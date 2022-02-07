# Use sieve of Eratosthenes to find nth prime, if answer is not found within sieve then return 0
def sieve_of_eratosthenes(sieve_size,n):
    sieve = [False]*(sieve_size+1)
    num_primes = 0
    for i in range(2,sieve_size+1):
        if sieve[i]:
            continue
        num_primes += 1
        if num_primes == n:
            return i
        for j in range(i*2,sieve_size,i):
            sieve[j] = True
    return 0

# Find nth prime using sieve of Eratosthenes, continue doubling sieve size until nth prime is found
def nth_prime(n):
    sieve_size = 1
    ans = 0
    while ans == 0:
        sieve_size*=2
        ans = sieve_of_eratosthenes(sieve_size,n)
    return ans

print(f"Result: {nth_prime(10001)}")
