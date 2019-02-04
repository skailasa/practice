import os

import numpy as np
import vtk


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
        """Return the 2x3 matrix of corners associated with an element."""
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


if __name__ == "__main__":

    g = Grid.from_vtk_file('data/lshape.vtk')

    print(g.vertices.shape)
    print(g.elements.shape)
    element_id = 1124
    print("Corners\n", g.get_corners(element_id))
    print("Jacobian \n", g.get_jacobian(element_id))
    #print(g.number_of_vertices)