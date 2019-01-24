"""
A*B = C

A is an N col K row matrix
B is a K col M row matrix
C (their product) is an M row by N col matrix
"""
import pyopencl as cl
import numpy as np


def matrix_mult(kernel_path, k=2, m=2, n=2, _max_arg=10):

    with open(kernel_path, 'r') as f:
        kernel = f.read()

    # Define matrices to be multiplied
    a = np.random.randint(0,
                          _max_arg,
                          size=(m, k)).astype(np.float64, order='F')

    b = np.random.randint(0,
                          _max_arg,
                          size=(k, n)).astype(np.float64, order='F')

    py_res = np.dot(a, b)
    c = np.zeros_like(py_res)

    # Define OpenCL params
    ctx = cl.create_some_context()
    q = cl.CommandQueue(ctx)
    mf = cl.mem_flags

    a_buf = cl.Buffer(
        ctx,
        mf.READ_ONLY | mf.COPY_HOST_PTR,
        hostbuf=a,
    )

    b_buf = cl.Buffer(
        ctx,
        mf.READ_ONLY | mf.COPY_HOST_PTR,
        hostbuf=b,
    )

    c_buf = cl.Buffer(
        ctx,
        mf.WRITE_ONLY,
        c.nbytes
    )

    prg = cl.Program(ctx, kernel).build()
    matMultKernel = prg.matMult

    KERNEL_ARGS = (np.int32(m), np.int32(n), np.int32(k), a_buf, b_buf, c_buf)
    matMultKernel(
        q, (m, n), None,
        *KERNEL_ARGS)

    cl.enqueue_copy(q, c, c_buf)

    result = "OpenCL: {} \n" \
             "NumPy: {}".format(c, py_res)

    print(result)


def main():
    matrix_mult('naive_matrix_mult.cl')


if __name__ == "__main__":
    main()