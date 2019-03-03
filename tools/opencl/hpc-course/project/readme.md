# HPC Project

We're trying to solve 

![poisson-eq](static/eq1.gif)

where 

![rhs](static/eq2.gif)

using the following discretisation

![discrete-operator](static/eq3.gif)

under the assumption that we can approximate

![sigma](static/eq4.gif)

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

or add to `.bashrc`