/*
Kernel for parallelising the spatial iteration in the 1D wave-equation
solver
*/
__kernel void wave_eq_1D(__global float *u2,
                         __global float *u1,
                         __global const float *u0,
                         float kappa,
                         float dt,
                         float dx)
{
	//Get total number of cells
	int nx = get_global_size(0);
	int i = get_global_id(0);

	//Calculate the indices of our neighbouring cells

	int center = i;
	int south = i + 1;
	int north = i - 1;

	//Internal cells
	if (i > 0 && i < nx - 1 )
		{
			u2[center] = 2 * u1[center] - u0[center] + kappa * (dt * dt) / (dx * dx) * (u1[north] - 2 * u1[center] + u1[south]);
		}
	//printf("u[%d]=%f \n", center, u2[center]);
}