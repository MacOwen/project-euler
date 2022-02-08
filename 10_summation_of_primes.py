# Find all primes under 2000000 using sieve of Eratosthenes
sieve = [False]*2000001
sum_primes = 2
# Only check odd numbers (the only even prime is 2, and it is preemptively added to the result)
for i in range(3,2000001,2):
    if sieve[i]:
        continue
    sum_primes += i
    for i in range(i*2, 2000001, i):
        sieve[i] = True

print(sum_primes)
