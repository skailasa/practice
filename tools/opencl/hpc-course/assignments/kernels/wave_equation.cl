/*
Kernel for parallelising the spatial iteration in the 1D wave-equation
solver
*/
__kernel void wave_eq_1D(__global float *u2,
                         __global const float *u1,
                         __global const float* u0,
                         float c,
                         float dt,
                         float dx)
{
	//Get total number of cells
	int nx = get_global_size(0);
	int idx = get_global_id(0);

	//Calculate the indices of our neighbouring cells
	int left;
	int right;

	if (idx == 0) {
	    left = 1;
	}
	else {
	    left = idx - 1;
	}
	if (idx == nx - 1) {
        right = nx - 1;
	}
	else {
	    right = idx + 1;
	}

	u2[idx] = 2 * u1[idx] \
                 - u0[idx] \
                 + (c*c) \
                    * (dt * dt) / (dx * dx) \
                    * (u1[right] - 2 * u1[idx] + u1[left]);
}