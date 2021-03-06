# HPC Project

We're trying to solve 

<p align="center">
    <img src="static/eq1.gif" alt="poisson-eq">
</p>

where 


<p align="center">
    <img src="static/eq2.gif" alt="rhs">
</p>

using the following discretisation

<p align="center">
    <img src="static/eq3.gif" alt="discretisation">
</p>

under the assumption that we can approximate

<p align="center">
    <img src="static/eq4.gif" alt="sigma">
</p>

i.e. by weighted means.

Here I've taken sigma to be a matrix of normally
distributed random numbers.


We can extend the analysis to solve the following parabolic equation:

<p align="center">
    <img src="static/parabolic.gif" alt="parabolic">
</p>

Using a simple forward discretisation in time

<p align="center">
    <img src="static/forward_time.gif" alt="time_disc">
</p>

This amounts to a model of time dependent diffusion.

Convergence relies on an appropriately chosen timestep sizes.

See [CFL Condition](https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition)

## Run poisson/diffusion solvers on OpenCL/Numpy

Create virtualenv running OpenCL, numpy and matplotlib.

```bash
python3 poisson.py
```

or 

```bash
python3 diffusion.py
```

No parameter parsing for now

## Run fenics code using docker

I've written a small bash script for running fenics scripts on their
docker container.

Run:

```bash
# If you don't have the fenics image
docker pull quay.io/fenicsproject/stable

# Add executable
chmod +x fenics

# Run python script in container
./fenics "python3 <my-fenics-script>.py"
```

The script mounts a volume to whichever directory you launch from
so you can copy over data etc from your simulation.

### Develop on Jupyter notebooks using docker

```bash
# Add fenics-jupyter script as executable
chmod +x fenics-jupyter

# Launch interactive container
./fenics-jupyter
```

From inside the container

```bash
# Launch jupyter server, and allow host access

jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

The server will be available on the host machine at `localhost:8888`