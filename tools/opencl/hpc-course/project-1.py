"""
Code to solve the poisson equation using FDM.
"""
from functools import partial

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import scipy.sparse.linalg as spla


SOLVERS = {
    "gmres": spla.gmres,
    "bicgstab": spla.bicgstab,
}


def fractional_sigma(sigma, i, j, M):
    """Find fractionally indexed values of sigma, using weigthed means"""

    sigma_i = 0.5 * (sigma[(i+1)*M + j]+sigma[i*M + j])
    sigma_i_minus = 0.5 * (sigma[(i-1)*M + j]+sigma[i*M + j])

    sigma_j = 0.5 * (sigma[i*M + j+1] + sigma[i*M + j])
    sigma_j_minus = 0.5 * (sigma[i*M + j-1] + sigma[i*M + j])

    return sigma_i, sigma_i_minus, sigma_j, sigma_j_minus


def differential_operator(u, dim):
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
                res[i*M+j] = h**2

    return res


def run_simulation(dim, solver):
    """Run simulation with a mesh of size 'dim' and given iterative method"""
    np.random.seed(1)

    operator = partial(differential_operator, dim=dim)

    A = spla.LinearOperator((dim**2, dim**2), operator)
    return SOLVERS[solver](A, rhs(dim))


def plot_simulation(dim, solver):
    """Run and plot simulation"""
    fig = plt.figure()
    ax = Axes3D(fig)

    x = np.arange(0,1,1/dim)
    y = np.arange(0,1,1/dim)

    sol = run_simulation(dim, solver)

    xs, ys = np.meshgrid(x, y)
    zs = sol[0].reshape((dim, dim))

    ax.plot_surface(xs, ys, -zs, rstride=1, cstride=1, cmap='hot')

    plt.show()


def main():
    plot_simulation(20, 'gmres')


if __name__ == "__main__":
    main()