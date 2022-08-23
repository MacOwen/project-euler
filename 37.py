# Find all prime numbers start <= i < n
def sieve(n,start):
  primes = []
  sieve = [False]*n
  for i in range(2,n):
    if sieve[i]:
      continue
    if i >= start:
      primes.append(i)
    for j in range(i*i,n,i):
      sieve[j] = True
  return primes

primes = set(sieve(1000000,11)) # Obtain all primes < 10^6

# Find all truncatable primes (assuming no truncatable primes >= 10^6)
truncatable_left = {2,3,5,7}
truncatable_right = {2,3,5,7}
for num in primes:
  left = int(str(num)[:-1])
  right = int(str(num)[1:])
  if left in truncatable_left:
    truncatable_left.add(num)
  if right in truncatable_right:
    truncatable_right.add(num)

# Combine sets and remove 1-digit primes
truncatable = truncatable_left & truncatable_right
truncatable -= {2,3,5,7}

ans = sum(truncatable)

print(ans)
