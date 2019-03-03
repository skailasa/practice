"""
Code to solve the poisson equation using FDM.
"""
from functools import partial

import matplotlib.pyplot as plt
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


def fractional_sigma(sigma, i, j, M):
    """Find fractionally indexed values of sigma, using weigthed means"""

    sigma_i = 0.5 * (sigma[(i+1)*M + j]+sigma[i*M + j])
    sigma_i_minus = 0.5 * (sigma[(i-1)*M + j]+sigma[i*M + j])

    sigma_j = 0.5 * (sigma[i*M + j+1] + sigma[i*M + j])
    sigma_j_minus = 0.5 * (sigma[i*M + j-1] + sigma[i*M + j])

    return sigma_i, sigma_i_minus, sigma_j, sigma_j_minus


def differential_operator_np(u, dim):
    """Apply the differential operator to a vector u"""
    # dimensions of solution vector
    M = dim  # rows
    N = dim   # cols

    mu, sigma = 0, 0.1
    np.random.seed(1)
    S = np.random.normal(mu, sigma, M*N)
    res = np.zeros(shape=(M*N,))

    # Calculate sigma
    sigma = np.exp(-S)

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


def differential_operator_cl(u, dim, kernel_fp):
    cl_ctx, cl_queue, mf = open_cl_setup()
    kernel_src = open(kernel_fp, 'r').read()

    # Calculate parameters of solution matrix
    m = np.int32(dim)  # rows
    n = np.int32(dim)   # cols

    # Calculate sigma
    mu, sigma = 0, 0.1
    np.random.seed(1)
    s = np.random.normal(mu, sigma, m*n)
    sigma = np.exp(-s)
    sigma = np.array(sigma, dtype=np.float64)

    # Upload data to the device
    u_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=u)
    sigma_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=sigma)

    # Allocate output buffer
    product_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE, u.nbytes)

    # Build kernel
    kernel_args = (m, n, sigma_gpu, u_gpu, product_gpu)
    prg = cl.Program(cl_ctx, kernel_src).build()
    mat_vec = prg.matVec

    # Execute kernel on device
    mat_vec(cl_queue, (m, n), None, *kernel_args)

    product = np.empty(m*n, dtype=np.float64)
    cl.enqueue_copy(cl_queue, product, product_gpu)

    return product


def run_simulation(dim, solver, method, kernel_fp):
    """
    Run simulation with a mesh of size 'dim' and given
    iterative method
    """

    if method == 'np':
        operator = partial(differential_operator_np, dim=dim)
    elif method == 'cl':
        operator = partial(
            differential_operator_cl, dim=dim, kernel_fp=kernel_fp
        )
    else:
        return "Must select valid solver method, 'np' or 'cl'"

    A = spla.LinearOperator((dim**2, dim**2), operator)
    return SOLVERS[solver](A, rhs(dim))


def plot_simulation(dim, solver, method, kernel_fp):
    """Run and plot simulation"""
    fig = plt.figure()
    ax = Axes3D(fig)

    x = np.arange(0,1,1/dim)
    y = np.arange(0,1,1/dim)

    sol = run_simulation(dim, solver, method, kernel_fp)

    xs, ys = np.meshgrid(x, y)
    zs = sol[0].reshape((dim, dim))

    ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, cmap='hot')

    plt.show()


def main(dim, solver, method, kernel_fp):
    plot_simulation(dim, solver, method, kernel_fp)


if __name__ == "__main__":
    dim = 100
    solver = 'gmres'
    method = 'cl'
    kernel_fp = 'kernels/poisson_equation_2d.cl'

    main(dim, solver, method, kernel_fp)