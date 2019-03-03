# HPC Project

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