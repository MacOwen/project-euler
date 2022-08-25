# Return all primes < n
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

primes = sieve(1000000)

# Created prefix sum of primes < 10^6 (prefix[i] = primes[0]+primes[2]+...+primes[i])
prefix = primes.copy()
for i in range(1,len(prefix)):
  prefix[i] += prefix[i-1]

# Attempt all possible consecutive sum ranges
ans = 0
longest = 0
primes = set(primes)
for i in range(len(prefix)):
  for j in range(i+1,len(prefix)):
    amt = prefix[j]
    if i!=0:
      amt -= prefix[i-1]
    if amt > 1000000:
      break
    if amt in primes:
      if j-i+1 > longest:
        longest = j-i+1
        ans = amt

print(ans)
