/*
Kernel for parallelising the spatial iteration in the 1D wave-equation
solver
*/
__kernel void wave_eq_1D(__global float *u2,
                         __global float *u1,
                         __global const float* u0,
                         float c,
                         float dt,
                         float dx)
{
	//Get total number of cells
	int nx = get_global_size(0);
	int index = get_global_id(0);

	//Calculate the indices of our neighbouring cells
	int left;
	int right;

	if (index == 0) {
	    left = 1;
	}
	else {
	    left = index - 1;
	}
	if (index == nx - 1) {
        right = nx - 1;
	}
	else {
	    right = index + 1;
	}
    u2[index] = 2 * u1[index] - u0[index] + (c*c) * (dt * dt) / (dx * dx) * (u1[right] - 2 * u1[index] + u1[left]);
}