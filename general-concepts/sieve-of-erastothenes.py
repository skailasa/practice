"""
Generate prime numbers between 1 and N

Seive of erastothenes:
    - loop through all numbers, keep list of current primes found, init
    with 2. (0, 1 implicit).
    - if current iterant has a prime with which it's a multiple then it
    is not prime
    - otherwise append it to the list of primes
"""


def check_prime(primes, i):
    for p in primes:
        if not i % p:
            return False
    return True


def seive(N):
    primes = [2]
    for i in range(3, N):
        if check_prime(primes, i):
            primes.append(i)
        else:
            pass
    return [0, 1]+primes


if __name__ == "__main__":
    #print(check_prime([2, 3, 5], ))
    print(seive(15))

