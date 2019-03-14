"""
Code to model a parabolic PDE using the spatial discretisation from
'poisson.py', and simple forward difference scheme in time.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import pyopencl as cl
from scipy.stats import multivariate_normal


def open_cl_setup():
    """Return objects required for interacting with OpenCL devices"""
    cl_ctx = cl.create_some_context()
    cl_queue = cl.CommandQueue(cl_ctx)
    mf = cl.mem_flags

    return cl_ctx, cl_queue, mf


def sigma_random(dim):
    """Random, normally distributed sigma values"""
    mu, sigma = 0, 0.1
    np.random.seed(1)
    S = np.random.normal(mu, sigma, dim*dim)

    return np.array(np.exp(-S), dtype=np.float32)


def gaussian(dim, centre=tuple([0.5, 0.5]), var=tuple([0.1, 0.1])):
    """
    Guassian defined over domain
    :param int dim: The dimension of the grid. i.e. how fine the mesh
        is.
    :param tuple[float, float] centre: The centre of the distribution in
        terms of the spatial domain of the grid.
    :param tuple[float, float] var: The variance in each dimension of
        the spatial domain.
    :return np.array(dim^2, ): The gaussian
    """
    x = np.arange(0, 1, 1 / dim)
    y = np.arange(0, 1, 1 / dim)
    xs, ys = np.meshgrid(x, y)

    xy = np.column_stack([xs.flat, ys.flat])

    mu = np.array(centre)
    sigma = np.array(var)

    covariance = np.diag(sigma ** 2)

    z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)

    for i in range(dim):
        for j in range(dim):
            if i == 0 or i == dim-1 or j == 0 or j == dim-1:
                z[i*dim+j] = 0

    return np.array(z, dtype=np.float32)


def run_simulation(kernel_fp, sigma, u0, dim, timesteps):
    """
    Run a simulation, returning final state of system after specified
    number of timesteps.

    :param str kernel_fp: The filepath to the kernel being used.
    :param np.array(dim^2,) sigma: The value of the weight matrix.
    :param np.array(dim^2,) u0: The initial conditions.
    :param int dim: The dimensions of the grid.
    :param int timesteps: The number of timesteps to simulate.
    :return np.array(dim^2,): The results of the simulation.
    """
    cl_ctx, cl_queue, mf = open_cl_setup()
    kernel_src = open(kernel_fp, 'r').read()

    # Upload data to the device
    u0_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=u0)
    sigma_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=sigma)

    # Allocate output buffer
    u1_gpu = cl.Buffer(cl_ctx, mf.READ_WRITE, u0.nbytes)

    # Build Kernels
    prg = cl.Program(cl_ctx, kernel_src).build()
    diffusion_kernel = prg.diffusion

    # Calculate time step
    dt = np.float32((1/dim)**2 / 4)

    for i in range(timesteps):
        kernel_args = (u1_gpu, u0_gpu, sigma_gpu, dt)
        diffusion_kernel(cl_queue, (dim, dim), None, *kernel_args)

        # Swap variables
        u0_gpu, u1_gpu = u1_gpu, u0_gpu

    # Copy back result
    result = np.empty_like(u0, dtype=np.float32)
    cl.enqueue_copy(cl_queue, result, u0_gpu)

    return result


def plot_simulation(kernel_fp, sigma, u0, dim, timesteps, axis):
    """
    Run and plot the simulation results
    :param str kernel_fp: The filepath to the kernel being used.
    :param np.array(dim^2,) sigma: The value of the weight matrix.
    :param np.array(dim^2,) u0: The initial conditions.
    :param int dim: The dimensions of the grid.
    :param int timesteps: The number of timesteps to simulate.
    :param str axis: '2d' or '3d' plot
    :return None:
    """

    res = run_simulation(kernel_fp, sigma, u0, dim, timesteps)
    res = res.reshape((dim, dim))

    if axis == '2d':
        plt.imshow(res, origin='lower', interpolation='none')

    elif axis == '3d':
        fig = plt.figure()
        ax = Axes3D(fig)
        x = np.arange(0, 1, 1 / dim)
        y = np.arange(0, 1, 1 / dim)
        xs, ys = np.meshgrid(x, y)
        ax.plot_surface(xs, ys, res, rstride=1, cstride=1, cmap='rainbow')

    plt.show()


if __name__ == "__main__":
    dim = 10
    kernel_fp = "kernels/diffusion.cl"
    timesteps = 50
    sigma = sigma_random(dim)
    u0 = gaussian(dim)

    plot_simulation(kernel_fp, sigma, u0, dim, timesteps, '3d')