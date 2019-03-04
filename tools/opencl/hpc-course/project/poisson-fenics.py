"""
Code to solve the Poisson equation using FeNics
"""


import numpy as np
from dolfin import *
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix


m, n = 100, 100

mesh = UnitSquareMesh(m, n)
V = FunctionSpace(mesh, "Lagrange", 1)


def on_boundary(x, on_boundary):
    return on_boundary


bc_value = Constant(0.0)
boundary_condition = DirichletBC(V, bc_value, on_boundary)

u = TrialFunction(V)
v = TestFunction(V)
f = Constant(1.0)

non_linear = Expression("1+x[0]*x[1]+x[1]*x[1]", element=V.ufl_element())

zero = Expression("0", element=V.ufl_element())
one = Expression("1", element=V.ufl_element())

a = inner(non_linear*grad(u), grad(v))*dx
L = f*v*dx

u = Function(V)
solve(a == L, u, boundary_condition)


#arr = u.vector().get_local()
#print(arr.shape)

import matplotlib.pyplot as plt
import matplotlib.tri as tri


def mesh2triang(mesh):
    xy = mesh.coordinates()
    return tri.Triangulation(xy[:, 0], xy[:, 1], mesh.cells())


C = u.compute_vertex_values(mesh)

plt.tripcolor(mesh2triang(mesh), C, shading='gouraud')
plt.axis('equal')
plt.savefig('poisson/test.png')