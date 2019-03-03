"""
(i) Implement a Grid class to read in triangular data
(ii) Solve the Wave Equation in 2D, and accellerate using OpenCL
"""
from time import time

import matplotlib.pyplot as plt
import numpy as np
import pyopencl as cl
import vtk


"""
Part (i) Implement Grid Class
"""


class Grid:
    """This class implements access to triangular grids."""

    def __init__(self, vertices, elements):
        """
        Initialize a grid.
        - Nx2 Numpy array of N vertices
        - Mx3 Numpy array with corresponding M elements
        """
        self._vertices = vertices
        self._elements = elements

    @classmethod
    def from_vtk_file(cls, filename):
        """Create a grid from a given vtk file."""

        # Instantiate reader object, read data
        reader = vtk.vtkUnstructuredGridReader()
        reader.SetFileName(filename)
        reader.Update()

        # Read in all data from file
        data = reader.GetOutput()

        # Store metadata
        vertex_data = data.GetPoints()
        n_vertices = vertex_data.GetNumberOfPoints()
        n_cells = data.GetNumberOfCells()

        # Create buffers for data
        vertices_buffer = np.zeros(shape=(n_vertices, 2))
        elements_buffer = []

        for idx in range(n_vertices):
            vertices_buffer[idx, :] = vertex_data.GetPoint(idx)[:2]

        for idx in range(n_cells):
            cell = data.GetCell(idx)
            if cell.GetCellType() == vtk.VTK_TRIANGLE:
                elements_buffer.append(
                    np.array(
                        [
                            cell.GetPointId(0),
                            cell.GetPointId(1),
                            cell.GetPointId(2),
                        ]
                    )
                )

        elements_buffer = np.array(elements_buffer)

        return cls(vertices_buffer, elements_buffer)

    @property
    def number_of_vertices(self):
        """Return the number of vertices."""
        return self._vertices.shape[0]

    @property
    def number_of_elements(self):
        """Return the number of elements."""
        return self._elements.shape[0]

    @property
    def vertices(self):
        """Return the vertices."""
        return self._vertices

    @property
    def elements(self):
        """Return the elements."""
        return self._elements

    def get_corners(self, element_id):
        """Return the 3x2 matrix of corners associated with an element."""
        return self._vertices[self._elements[element_id, :], :]

    def get_jacobian(self, element_id):
        """Return the jacobian associated with a given element id."""
        corners = self.get_corners(element_id)
        a, b, c = corners[0], corners[1], corners[2]

        x_a, y_a = a[0], a[1]
        x_b, y_b = b[0], b[1]
        x_c, y_c = c[0], c[1]

        jacobian = [[x_b-x_a, y_b-y_a], [x_c-x_a, y_c-y_a]]

        return np.array(jacobian)

    def export_to_vtk(self, fname, point_data=None):
        """Export grid to a vtk file. Optionally also export point data."""

        grid = vtk.vtkUnstructuredGrid()

        if point_data is not None:

            data = grid.GetPointData()
            scalar_data = vtk.vtkDoubleArray()
            scalar_data.SetNumberOfValues(len(point_data))
            for index, value in enumerate(point_data):
                scalar_data.SetValue(index, value)
            data.SetScalars(scalar_data)

        points = vtk.vtkPoints()
        points.SetNumberOfPoints(self.number_of_vertices)
        for index in range(self.number_of_vertices):
            points.InsertPoint(
                index,
                (self.vertices[0, index], self.vertices[1, index], 0))

        grid.SetPoints(points)

        for index in range(self.number_of_elements):
            grid.InsertNextCell(
                vtk.VTK_TRIANGLE, 3,
                [self.elements[0, index], self.elements[1, index],
                 self.elements[2, index]]
            )

        writer = vtk.vtkUnstructuredGridWriter()
        writer.SetFileName(fname)
        writer.SetInputData(grid)
        writer.Write()

        return grid


"""
Part (ii) Implement Solution to the Wave Equation
"""


def open_cl_setup():
    """
    Return objects required for interacting with OpenCL devices
    """
    cl_ctx = cl.create_some_context()
    cl_queue = cl.CommandQueue(cl_ctx)
    mf = cl.mem_flags

    return cl_ctx, cl_queue, mf


def solve_wave_equation_cl(
        kernel_fp = 'kernels/wave_equation.cl', nx=200, nt=500, c=1, T=2, X=1):
    """
    Solve the 1D wave equation using OpenCL
    :param nx: The number of spatial steps
    :param nt: The number of temporal steps
    :param c: Wave speed
    :param T: Simulation time
    :param X: Spatial extent
    :return None:
    """
    cl_ctx, cl_queue, mf = open_cl_setup()
    kernel_src = open(kernel_fp, 'r').read()

    # Calculate step size
    dx = X/(nx-1)
    dt = T/nt

    # Calculate Courant number
    C = c * (dt / dx)

    # CPU data
    xx = np.linspace(0, X, nx, dtype=np.float32)
    u0 = np.exp(-5*(xx-.5) ** 2)

    # Calculate first step
    u1 = np.zeros_like(u0, dtype=np.float32)
    for i in range(0, nx):
        il = 1 if i == 0 else i - 1
        ir = nx - 2 if i == nx - 1 else i + 1
        u1[i] = u0[i] - 0.5 * C**2 * (u0[ir] - 2*u0[i] + u0[il])

    # Upload data to the device
    U0_g = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=u0)
    U1_g = cl.Buffer(cl_ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=u1)

    # Allocate output buffer
    U2_g = cl.Buffer(cl_ctx, mf.READ_WRITE, u1.nbytes)

    # Build Kernels
    prg = cl.Program(cl_ctx, kernel_src).build()
    wave_equation_1d = prg.wave_eq_1D

    res = [u0, u1]

    # Loop through all the timesteps
    for i in range(1, nt):
        kernel_args = (U2_g, U1_g, U0_g, np.float32(c), np.float32(dt), np.float32(dx))

        # Execute kernel on device with nx threads
        wave_equation_1d(cl_queue, (nx, 1), None, *kernel_args)

        u2 = np.empty(nx, dtype=np.float32)
        cl.enqueue_copy(cl_queue, u2, U2_g)
        res.append(u2)

        # Swap variables
        U0_g, U1_g, U2_g = U1_g, U2_g, U0_g

    res = np.array(res).T

    return res


def plot_simulation(
        kernel_fp='kernels/wave_equation.cl', nx=200, nt=500, c=1, T=2, X=1):
    """Plot OpenCL simulation experiment results"""

    start = time()
    res = solve_wave_equation_cl(kernel_fp, nx, nt, c, T, X)
    print("Simulation time {:.2f} seconds".format(time()-start))

    plt.imshow(res, extent=[0, T, 0, X])
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    kwargs = dict(kernel_fp='kernels/wave_equation.cl',
                  nx=200, nt=500, c=1, T=2, X=1)
    plot_simulation(**kwargs)

