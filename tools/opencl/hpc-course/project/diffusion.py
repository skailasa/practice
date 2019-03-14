"""
Code to model a parabolic PDE using the spatial discretisation from
'poisson.py', and simple forward difference scheme in time.
"""

import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

import numpy as np
import pyopencl as cl


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

    return np.array(np.exp(-S), dtype=np.float32)


def run_simulation(kernel_fp, sigma, u0, dim, nt=30):

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

    dt = (1/dim)**2 / 4

    for i in range(nt):
        kernel_args = (u1_gpu, u0_gpu, sigma_gpu, np.float32(dt))
        diffusion_kernel(cl_queue, (dim, dim), None, *kernel_args)

        # Swap variables
        u0_gpu, u1_gpu = u1_gpu, u0_gpu

    result = np.empty_like(u0, dtype=np.float32)
    cl.enqueue_copy(cl_queue, result, u0_gpu)

    return result


def gaussian(dim):
    """Guassian defined over domain"""
    x = np.arange(0, 1, 1 / dim)
    y = np.arange(0, 1, 1 / dim)
    xs, ys = np.meshgrid(x, y)

    xy = np.column_stack([xs.flat, ys.flat])

    mu = np.array([0.0, 0.0])

    sigma = np.array([.5, .5])
    covariance = np.diag(sigma ** 2)

    z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)

    return np.array(z, dtype=np.float32)


def main():
    dim = 10
    kernel_fp = "kernels/diffusion.cl"
    sigma = sigma_random(dim)
    u0 = gaussian(dim)

    res = run_simulation(kernel_fp, sigma, u0, dim)

    plt.imshow(res.reshape((dim, dim)), origin='lower', interpolation='none')
    plt.show()


if __name__ == "__main__":
    main()