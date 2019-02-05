/*
Impose Dirichlet boundary conditions on wave equation solver
*/

__kernel void wave_eq_2D_bc(__global float *u) {
	//Get total number of cells
	int nx = get_global_size(0);
	int i = get_global_id(0);

	//Calculate the 2 indices of our neighbouring cells
	int center = i;
	int north = nx + i;
	int south = nx - i;

	if (i == 0) {
		u[center] = u[south];
	}
	else if (i == nx - 1) {
		u[center] = u[north];
	}
	//printf("u[%d]=%f \n", center, u[center]);
}

