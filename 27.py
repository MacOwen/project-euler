import math

# Find all primes < N
def sieve(n):
  primes = []
  sieve = [False]*n
  for i in range(2,int(math.sqrt(n))+1):
    if sieve[i]:
      continue
    primes.append(i)
    for j in range(i*i,n,i):
      sieve[j] = True
  return primes

def is_prime(n):
  if n < 2:
    return False
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True

# Test all a-coefficients from -999 to 999, and b-coefficients from -1000 to 1000
# n^2 + an + b
ans = 0
best = 0
for a in range(-999,1000):
  # b >= 2 (to satisfy first term with n^2+an = 0)
  for b in range(2,1001):
    n = 0
    while is_prime(n*n+a*n+b):
      n += 1
    if n > best:
      best = n
      ans = a*b

print(ans)
