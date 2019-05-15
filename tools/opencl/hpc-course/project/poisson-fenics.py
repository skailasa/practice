"""
Code to solve the Poisson equation using Fenics FRM
"""
from dolfin import *
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from mpl_toolkits.mplot3d import axes3d, Axes3D


def on_boundary(x, on_boundary):
    """Define dirichlet boundary conditions for dolfin"""
    return on_boundary


def mesh2triang(mesh):
    """Convert mesh to triangle vertices"""
    xy = mesh.coordinates()
    return tri.Triangulation(xy[:, 0], xy[:, 1], mesh.cells())


def run_simulation_fenics(dim):
    """Run simulation for a specified mesh size"""
    m = dim  # rows
    n = dim  # cols

    # Create mesh and function space
    mesh = UnitSquareMesh(m, n)
    V = FunctionSpace(mesh, "Lagrange", 1)

    # Set dirichlet boundary conditions
    bc_value = Constant(0.0)
    boundary_condition = DirichletBC(V, bc_value, on_boundary)

    # Set trial and test functions
    u = TrialFunction(V)
    v = TestFunction(V)

    # Set source term (rhs)
    f = Constant(1.0)

    # Add nonlinearity to test correctness of OpenCL implementation
    non_linear = Expression("1+x[0]*x[1]+x[1]*x[1]", element=V.ufl_element())

    # Solve using FEM
    a = inner(non_linear*grad(u), grad(v))*dx
    L = f*v*dx

    u = Function(V)
    solve(a == L, u, boundary_condition)

    return u, mesh


def plot_simulation_fenics(dim, plot_type):
    """Run and plot simulation"""
    u, mesh = run_simulation(dim)

    C = u.compute_vertex_values(mesh)

    fig = plt.figure()

    if plot_type == '3d':
        ax = Axes3D(fig)
        ax.plot_trisurf(mesh2triang(mesh), C, linewidth=0.2, antialiased=True)

    elif plot_type == '2d':
        plt.tripcolor(mesh2triang(mesh), C, shading='gouraud')

    else:
        return "must enter plotting type '2d' or '3d'"

    plt.axis('equal')
    plt.savefig('poisson/test.png')


def main():
    plot_simulation(10, plot_type='2d')


if __name__ == "__main__":
    main()