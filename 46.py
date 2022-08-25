# Find all primes < n
def sieve(n):
  primes = []
  sieve = [False]*n
  for i in range(2,n):
    if sieve[i]:
      continue
    primes.append(i)
    for j in range(i*i,n,i):
      sieve[j] = True
  return primes

# Find all invalid numbers < n
def all_invalid(n):
  primes = sieve(n)
  # Set prime and odd numbers as "reachable" (to avoid counting towards the answer)
  reachable = [False]*n
  for prime in primes:
    reachable[prime] = True
  for i in range(n):
    if i%2==0:
      reachable[i] = True
  # For each prime, 
  for prime in primes:
    i=1
    while prime+2*i*i < n:
      reachable[prime+2*i*i] = True
      i += 1
  # Find all non-reachable
  ans = []
  for i in range(n):
    if not reachable[i] and i>1:
      ans.append(i)
  return ans

ans = all_invalid(10000)[0]

print(ans)
