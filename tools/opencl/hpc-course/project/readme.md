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

## Run poisson solver on OpenCL/Numpy

Create virtualenv running OpenCL, numpy and matplotlib.

```bash
python3 poisson.py
```

No parameter parsing for now

## Run fenics code using docker

I've written a small bash script for running fenics scripts on their
docker container.

Run:

```bash
chmod +x fenics
./fenics "python3 <my-fenics-script>.py
```

or add the fenics command to `.bashrc`