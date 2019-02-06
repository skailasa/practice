import time

import pyopencl as cl
import numpy as np
import numba

CTX = cl.create_some_context()
QUEUE = cl.CommandQueue(CTX)
KERNEL = open('kernels/potential_kernel.cl', 'r').read()


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start


@numba.jit
def evaluate_field_numpy(evaluation_points,
                         source_positions,
                         strength_vector):
    res = np.zeros(shape=(len(evaluation_points),))

    for idx in range(len(evaluation_points)):
        res[idx] = -np.dot(
            strength_vector,
            np.log(
                np.linalg.norm(
                    source_positions - evaluation_points[idx],
                    axis=1
                )
            )
        )
    return res


def evaluate_field_opencl(evaluation_points,
                          source_positions,
                          strength_vector):

    mf = cl.mem_flags
    n_eval_points = evaluation_points.shape[0]
    n_source_positions = source_positions.shape[0]

    # copying from the host device is automatic
    eval_buffer = cl.Buffer(
        CTX,
        mf.COPY_HOST_PTR | mf.READ_ONLY,
        hostbuf=evaluation_points
    )

    source_buffer = cl.Buffer(
        CTX,
        mf.COPY_HOST_PTR | mf.READ_ONLY,
        hostbuf=source_positions
    )

    strength_buffer = cl.Buffer(
        CTX,
        mf.COPY_HOST_PTR | mf.READ_ONLY,
        hostbuf=strength_vector
    )

    result_buffer = cl.Buffer(
        CTX,
        mf.ALLOC_HOST_PTR,
        size=evaluation_points.shape[0] * 8
    )  # links host and device results

    prg = cl.Program(CTX, KERNEL).build()
    potential_kernel = prg.evaluate_potential

    potential_kernel(QUEUE,
                     (n_eval_points,),
                     (1,),
                     eval_buffer,
                     source_buffer,
                     strength_buffer,
                     result_buffer
                     )

    result, _ = cl.enqueue_map_buffer(
        QUEUE,
        result_buffer,
        cl.map_flags.READ,
        0,  # offset, where buffer read starts
        (n_eval_points,),  # python result shape
        np.double,  # numpy type
    )

    QUEUE.finish()

    return result


def main():
    Nx = 100
    Ny = 100
    xpoints, ypoints = np.mgrid[0: 1: 1j * Nx, 0: 1: 1j * Ny]
    _temp = np.vstack([xpoints.ravel(), ypoints.ravel()]).T

    EVALUATION_POINTS = np.zeros(shape=_temp.shape)
    EVALUATION_POINTS[:] = _temp

    N = 100  # number of particles
    RAND = np.random.RandomState(0)  # random seed
    POS = RAND.rand(N, 2)  # source positions
    K = RAND.rand(N)  # strength vector

    result_opencl = evaluate_field_opencl(EVALUATION_POINTS, POS, K)
    result_numba = evaluate_field_numpy(EVALUATION_POINTS, POS, K)
    idx = 21
    print(result_opencl[idx])
    print(result_numba[idx])


if __name__ == "__main__":
    main()