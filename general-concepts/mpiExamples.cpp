#include <iostream>
#include <mpi.h>
#include <math.h>
#include <random>
#include <vector>
#include <algorithm>

// Find a prime
bool IsPrime(unsigned candidate)
{
  bool isPrime = true;
  if (candidate == 0 || candidate == 1)
  {
    isPrime = false;
  }
  else if (candidate == 2)
  {
    isPrime = true;
  }
  else
  {
    unsigned limit = static_cast<unsigned>(ceil(sqrt(static_cast<double>(candidate))));
    for (unsigned factor(2); factor <= limit; ++factor)
    {
      if (candidate % factor == 0)
      {
        isPrime = false;
        break;
      }
    }
  }
  return isPrime;
}

// Point to point communication
void computePrimesInParallel1P2P() {
		// Random number generation
 	std::minstd_rand generator;
	unsigned min(0), max(1000);
	std::uniform_int_distribution<> distribution(min, max);

	// Create buffer to store prime number candidates
	std::vector<unsigned> candidates(size - 1);

	// Buffer to store the prime that is found
	int found_prime(0);

	// Main loop continues until a prime is found
	while (found_prime == 0) {
    	if (rank == 0) {
            // Generate some candidate numbers for each process to test
            std::generate(candidates.begin(), candidates.end(),
                          [&]() { return distribution(generator); });

            // Send one to each worker, don't send one to master
            for (int worker(1); worker < size; ++worker) {
                MPI_Ssend(&candidates[worker - 1], 1, MPI_UNSIGNED,
                		  worker, 0, MPI_COMM_WORLD);
            }

            // Receive result of prime check
            for (int worker(1); worker < size; ++worker) {
                unsigned result;
                MPI_Recv(&result, 1, MPI_UNSIGNED, worker, 0,
                         MPI_COMM_WORLD, MPI_STATUS_IGNORE);
                if (result == 1) {
                    found_prime = candidates[worker - 1];
                    std::cout << "Worker " << worker << " found prime "
                              << found_prime << std::endl;
                }
            }
    	} else {
            // Receive the candidate to check
            unsigned candidate;
            MPI_Recv(&candidate, 1, MPI_UNSIGNED, 0, 0, 
            		 MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            // Do the check
            unsigned is_prime = IsPrime(candidate) ? 1 : 0;
            // Return the result
            MPI_Ssend(&is_prime, 1, MPI_UNSIGNED, 0, 0, MPI_COMM_WORLD);
            if (is_prime == 1) {
                found_prime = candidate;
            }
        }
    }
}

// Collective communication
void computePrimesInParallelCollective() {
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Random number generation
    std::minstd_rand generator;
    unsigned min(22), max(100);
    std::uniform_int_distribution<> distribution(min, max);

    // Calculate elements per process
    unsigned long elementsPerProcess = 1;

    unsigned found_prime(0);
    while (found_prime == 0) {

        std::vector<unsigned> subsetOfArray(elementsPerProcess);
        std::vector<unsigned> candidates(size);

        // Generate candidates to check for primality
        // Create some candidate numbers for each process to test
        std::generate(candidates.begin(), candidates.end(),
                      [&]() { return distribution(generator); });

        std::cout << "number of candidate: " << candidates.size() << std::endl;

        // Scatter accross all processes including root
        MPI_Scatter(candidates.data(), elementsPerProcess, MPI_UNSIGNED,
                    subsetOfArray.data(), elementsPerProcess, MPI_UNSIGNED,
                    0, MPI_COMM_WORLD);

        // Loop is extraneous as we only have one element per process, but this is flexible
        for (int i(0); i < subsetOfArray.size(); i++) {

            std::cout << "checking: " << subsetOfArray[i] << " at proc: " << rank << std::endl;
            int isPrime = IsPrime(subsetOfArray[i])  ? 1 : 0;
            std::cout << "result: " << isPrime << std::endl;

            if (IsPrime(subsetOfArray[i])) {
                found_prime = subsetOfArray[i];
                std::cout << "Found prime: " << found_prime << " at proc: " << rank << std::endl;

                // One we've found a prime, broadcast this news back to all other procs
                MPI_Bcast(&found_prime, 1, MPI_UNSIGNED, rank, MPI_COMM_WORLD);
            }
        }

        // Check if there has been any news regarding primes, if so put into global prime
        int global_prime;
        MPI_Allgather(
                &found_prime,
                1,
                MPI_UNSIGNED,
                &global_prime,
                1,
                MPI_UNSIGNED,
                MPI_COMM_WORLD
        );

        // Break out of loop if we've found a prime globally
        if (global_prime != 0) {
            std::cout << "global prime: " << global_prime << std::endl;
            found_prime = global_prime;
        }
    }
}

void sendRecvExample() {

    int myid, numprocs, left, right;
    int buffer = 1;
    int buffer2 = 0;

    MPI_Request request;
    MPI_Status status;
 
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);
 
    right = (myid + 1) % numprocs;
    left = myid - 1;
    if (left < 0)
        left = numprocs - 1;
 
    int error = MPI_Sendrecv(
        &buffer, 1, MPI_INT, left, 123,
        &buffer2, 1, MPI_INT, right, 123,
        MPI_COMM_WORLD, &status);
}

void reduceExample() {
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    const int TERMS_PER_PROCESS = 1000;
    double my_denominator = rank * TERMS_PER_PROCESS * 2 + 1;
    double sign = 1;
    double my_result = 0.0;
    for (int i(0); i<TERMS_PER_PROCESS; ++i)
    {
        my_result += sign / my_denominator;
        my_denominator += 2;
        sign = -sign;
    }

    // Parallel reduction code goes here
    double result;
    int error = MPI_Reduce(&my_result, &result, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
}



void main(int argc, char* argv[])
{
   /***********************Ignore this stuff***********************/
    MPI_Init(&argc, &argv);
	
    int world_rank, world_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size)
    /****************************************************************/
    computePrimesInParallelP2p();
    computePrimesInParallelCollective();
    /***********************Ignore this stuff***********************/
    MPI_Finalize();
    /****************************************************************/
}