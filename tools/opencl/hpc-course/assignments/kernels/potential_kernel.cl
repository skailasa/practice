/*
Kernel for evaluation a potential field at a specified set of points.
*/

__kernel void evaluate_potential(__global double *evaluationPoints,
                                   __global double *sourcePositions,
                                   __global double *strengthVector,
                                   __global double *result)
    {
        const int gid = get_global_id(0);

        float evaluationPointX = evaluationPoints[2*gid];
        float evaluationPointY = evaluationPoints[2*gid+1];
        int numberOfParticles = 100;

        // counter to store result
        float res = 0.0;
        // evaluate summation of potential for a given evaluation point.
        for (int i=0; i < numberOfParticles; i++) {
            float distance = sqrt(
                (float)powf((sourcePositions[2*i]-evaluationPointX), 2) +
                (float)powf((sourcePositions[2*i+1]-evaluationPointY), 2)
                );

            if (distance == 0) {
            }
            else {
                res += strengthVector[i] * log(distance);
            }
        }
        // Store the result
        result[gid] = -res;
    }