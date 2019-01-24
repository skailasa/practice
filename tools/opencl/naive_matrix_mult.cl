__kernel void matMult (const int M, const int N, const int K,
                          __global double* A, __global double* B,
                          __global double* C)
{
    int Row = get_global_id(0);
    int Col = get_global_id(1);

    double res = 0;

    for (int k = 0; k<K; k++) {
        res += A[k*M + Row] * B[Col*K + k];
    }
    C[Row*M + Col] = res;
}