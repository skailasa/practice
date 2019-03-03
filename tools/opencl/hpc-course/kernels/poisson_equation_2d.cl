/*
Kernel for parallelising the matrix vector product for the solution of the 2D
poisson-equation solver
*/


__kernel void matVec(const int M, const int N,
                     const __global double* sigma,
                     const __global double* u,
                     __global double* product
                            ) {

    // Thread identifiers
    //const int i = 2*get_global_id(0); // Row ID of product (0..M)
    //const int j = 2*get_global_id(0)+1; // Col ID of product (0..N)

    const int i = get_global_id(0);
    const int j = get_global_id(1);

    // For a single element in the result
    double res;
    if (i == 0 || i == M-1 || j == 0 || j == N-1) {
            res = u[i*M + j];
        }
    else {
            double si;
            double sim;
            double sj;
            double sjm;
            double alpha;

            si = 0.5 * (sigma[(i+1)*M + j]+sigma[i*M + j]);
            sim = 0.5 * (sigma[(i-1)*M + j]+sigma[i*M + j]);
            sj = 0.5 * (sigma[i*M + j+1] + sigma[i*M + j]);
            sjm =  0.5 * (sigma[i*M + j-1] + sigma[i*M + j]);

            alpha = si + sim + sj + sjm;

            res = (
                si*u[(i+1)*M+j]
                + sim*u[(i-1)*M+j]
                + sj*u[i*M+j+1]
                + sjm*u[i*M+j-1]
                - alpha*u[i*M+j]
            );

        }

    // Store the result
    product[i*M+j] = res;
    }