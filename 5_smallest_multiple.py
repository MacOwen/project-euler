import math

def prime_factors(x):
    # Using sieve of Eratosthenes, mark all multiples of prime numbers as non-prime
    sieve = [False]*(x+1)
    for i in range(2,x+1):
        if sieve[i]:
            continue
        for j in range(i*2,x+1,i):
            sieve[j] = True
    # Return non-marked numbers (primes)
    factors = []
    for i in range(2,x+1):
        if not sieve[i]:
            factors.append(i)
    return factors

def smallest_multiple(x):
    # Find all prime numbers <= x
    factors = prime_factors(x)
    # For each prime, find the largest power that fits into x, then return the product of all numbers
    ans = 1
    for factor in factors:
        while factor*factor <= x:
            factor *= factor
        ans *= factor
    return ans

print(f"Result: {smallest_multiple(20)}")
