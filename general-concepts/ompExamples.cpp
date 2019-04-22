unsigned SumUsingParallelFor(const std::vector<unsigned>& values)
{
  // Implement me using OpenMPs parallel for construct.
    unsigned int res = 0;

    #pragma omp parallel shared(res), shared(values)
    {
        #pragma omp for
        for (int i = 0; i<values.size(); i++) {
            res += values[i];
        }
    }
    return res;
}


unsigned SumUsingReduction(const std::vector<unsigned>& values)
{
  // Implement me using OpenMPs reduction on sum.
  unsigned int res = 0;

  #pragma omp parallel shared(values), reduction(+:res)
  {
    #pragma omp for
      for (int i = 0; i < values.size(); i++) {
          res += values[i];
      }
  }
  return res;
}