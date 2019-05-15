"""
Code to solve the poisson equation using FDM.

This script implements a Numpy as well as an OpenCL solver
"""
from functools import partial

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import scipy.sparse.linalg as spla
import pyopencl as cl


SOLVERS = {
    "gmres": spla.gmres,
    "bicgstab": spla.bicgstab,
}


def open_cl_setup():
    """
    Return objects required for interacting with OpenCL devices
    """
    cl_ctx = cl.create_some_context()
    cl_queue = cl.CommandQueue(cl_ctx)
    mf = cl.mem_flags

    return cl_ctx, cl_queue, mf


def sigma_random(dim):
    """Random, normally distributed sigma values"""
    mu, sigma = 0, 0.1
    np.random.seed(1)
    S = np.random.normal(mu, sigma, dim*dim)

    return np.exp(-S)


def sigma_polynomial(dim):
    """
    Sigma values given by applying equation f(x, y)=1+x^2+y, for
    validation
    """
    x = np.arange(0, 1, 1/dim)
    y = np.arange(0, 1, 1/dim)
    xs, ys = np.meshgrid(x, y)
    return (1 + xs**2 + ys**2).flatten()


def fractional_sigma(sigma, i, j, M):
    """Find fractionally indexed values of sigma, using weigthed means"""

    sigma_i = 0.5 * (sigma[(i+1)*M + j]+sigma[i*M + j])
    sigma_i_minus = 0.5 * (sigma[(i-1)*M + j]+sigma[i*M + j])

    sigma_j = 0.5 * (sigma[i*M + j+1] + sigma[i*M + j])
    sigma_j_minus = 0.5 * (sigma[i*M + j-1] + sigma[i*M + j])

    return sigma_i, sigma_i_minus, sigma_j, sigma_j_minus


def differential_operator_np(u, dim, sigma_type):
    """
    Apply the differential operator to a vector u using Numpy arrays
    """
    # dimensions of solution vector
    M = dim  # rows
    N = dim   # cols

    if sigma_type == 'random':
        sigma = sigma_random(dim)
    elif sigma_type == 'polynomial':
        sigma = sigma_polynomial(dim)
    else:
        return "Must select valid sigma type"

    # buffer for result of linear operator application
    res = np.zeros(shape=(M*N,))

    for i in range(M):
        for j in range(N):
            if i == 0 or i == M-1 or j == 0 or j == N - 1:
                res[i*M+j] = u[i*M+j]  # boundary conditions

            else:
                si, sim, sj, sjm = fractional_sigma(sigma, i, j, M)
                alpha = si + sim + sj + sjm

                res[i*M+j] = (
                        + si*u[(i+1)*M+j]
                        + sim*u[(i-1)*M+j]
                        + sj*u[i*M+j+1]
                        + sjm*u[i*M+j-1]
                        - alpha*u[i*M+j]
                )
    return res


def rhs(dim):
    """Calculate the rhs encapsulating initial/boundary conditions"""
    M = dim  # rows
    N = dim   # cols
    h = 1/dim

    res = np.zeros(shape=(M*N,))

    for i in range(M):
        for j in range(N):
            if i == 0 or i == M-1 or j == 0 or j == N - 1:
                res[i*M+j] = 0  # boundary conditions
            else:
                res[i*M+j] = -h**2

    return res


def differential_operator_cl(u, dim, kernel_fp, sigma_type):
    """
    Apply the differential operator to a vector u using OpenCL
    """
    cl_ctx, cl_queue, mf = open_cl_setup()
    kernel_src = open(kernel_fp, 'r').read()

    # Calculate parameters of solution matrix
    m = np.int32(dim)  # rows
    n = np.int32(dim)   # cols

    # Calculate sigma
    if sigma_type == 'random':
        sigma = sigma_random(dim)
    elif sigma_type == 'polynomial':
        sigma = sigma_polynomial(dim)
    else:
        return "Must select valid sigma type"

    # Upload data to the device
    u_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=u)
    sigma_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=sigma)

    # Allocate output buffer
    product_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE, u.nbytes)

    # Build kernel
    tile_size = 1
    global_work_group = (m, n)
    local_work_group = (tile_size, tile_size)
    kernel_args = (m, n, sigma_gpu, u_gpu, product_gpu)
    prg = cl.Program(cl_ctx, kernel_src).build()
    mat_vec = prg.matVec

    # Execute kernel on device

    mat_vec(cl_queue, global_work_group, local_work_group, *kernel_args)

    product = np.empty(m*n, dtype=np.float64)
    cl.enqueue_copy(cl_queue, product, product_gpu)

    return product


def run_simulation(dim, solver, method, kernel_fp, sigma_type):
    """
    Run simulation with a mesh of size 'dim' and given iterative method
    """

    if method == 'np':
        operator = partial(
            differential_operator_np,
            dim=dim,
            sigma_type=sigma_type
        )

    elif method == 'cl':
        operator = partial(
            differential_operator_cl,
            dim=dim,
            kernel_fp=kernel_fp,
            sigma_type=sigma_type
        )

    else:
        return "Must select valid solver method, 'np' or 'cl'"

    A = spla.LinearOperator((dim**2, dim**2), operator)
    return SOLVERS[solver](A, rhs(dim))


def analytic_solution(dim):
    """Analytic solution of poisson equation with a point source"""
    x = np.arange(0, 1+1/dim, 1/dim)
    y = np.arange(0, 1+1/dim, 1/dim)
    xs, ys = np.meshgrid(x, y)

    xs = xs.flatten()
    ys = ys.flatten()
    sol = np.divide(1, np.sqrt((xs-0.501)**2+(ys-0.5)**2))

    return (xs.reshape((dim+1, dim+1)),
            ys.reshape((dim+1, dim+1)),
            sol.reshape((dim+1,dim+1)))


def plot_analytic_solution(dim):
    """
    Find and plot an approximation of an analytic soln with a point
    source
    """
    xs, ys, sol = analytic_solution(dim)

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.plot_surface(xs, ys, sol, rstride=1, cstride=1, cmap=cm.rainbow)
    ax.set_title("Analytic solution with point source")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.show()


def plot_simulation(dim, solver, method, kernel_fp, sigma_type, plot_type):
    """Run and plot simulation"""

    x = np.arange(0, 1, 1/dim)
    y = np.arange(0, 1, 1/dim)
    sol = run_simulation(dim, solver, method, kernel_fp, sigma_type)
    zs = sol[0].reshape((dim, dim))
    fig = plt.figure()

    if plot_type == '3d':
        ax = Axes3D(fig)
        xs, ys = np.meshgrid(x, y)
        ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, cmap='rainbow')
        plt.show()

    elif plot_type == '2d':
        plt.imshow(zs, origin='lower', interpolation='none')
        plt.show()

    else:
        return "Must select valid plot type"


if __name__ == "__main__":
    dim = 10
    solver = 'gmres'
    method = 'cl'
    sigma_type='polynomial'
    plot_type='2d'
    kernel_fp = 'project/kernels/matvec.cl'

    plot_simulation(dim, solver, method, kernel_fp, sigma_type, plot_type)

    #plot_analytic_solution(dim)
