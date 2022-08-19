# Return a list of all primes <= n
def sieve(n):
  sieve = [False]*(n+1)
  sieve[0] = True
  sieve[1] = True
  primes = []
  for i in range(2,n+1):
    if sieve[i]:
      continue
    primes.append(i)
    for j in range(i*i, n+1, i):
      sieve[j] = True
  return primes

n = 1
primes = sieve(n)
while len(primes)<10001:
  n *= 2
  primes = sieve(n)

print(primes[10000])
