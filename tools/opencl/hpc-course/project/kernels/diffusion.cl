/*
Kernel to solve the time dependent diffusion equation, for part 2 of the
project, using the spatial discretisation from part 1.
*/


__kernel void diffusion(__global float* u1,
                        __global float* u0,
                         const __global float* sigma,
                         const float dt) {


    // Size of global problem
    const int M = get_global_size(0);
    const int N = get_global_size(1);

    // Spatial step size
    const float h = 1./M;

    // Thread identifiers
    const int i = get_global_id(0);
    const int j = get_global_id(1);

    // For a single element in the result
    if (i == 0 || i == M-1 || j == 0 || j == N-1) {
            // Boundary conditions
            u1[i*M+j] = 0;

    } else {
            // Internal cells
            double si;
            double sim;
            double sj;
            double sjm;
            double u0c;
            double u0i;
            double u0im;
            double u0j;
            double u0jm;

            si = 0.5 * (sigma[(i+1)*M + j]+sigma[i*M + j]);
            sim = 0.5 * (sigma[(i-1)*M + j]+sigma[i*M + j]);
            sj = 0.5 * (sigma[i*M + j+1] + sigma[i*M + j]);
            sjm =  0.5 * (sigma[i*M + j-1] + sigma[i*M + j]);

            u0c = u0[i*M+j];
            u0i = u0[(i+1)*M+j];
            u0im = u0[(i-1)*M+j];
            u0j = u0[i*M+j+1];
            u0jm = u0[i*M+j-1];

            u1[i*M+j] = u0[i*M+j]
                        + dt/(h*h) * ((si*(u0i-u0c) - sim*(u0c-u0im))
                                     +(sj*(u0j-u0c) - sjm*(u0c-u0jm)));

    }
}