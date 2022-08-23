import math

illegal_digits = {0,2,4,5,6,8}

# Find all primes < N (without any zeros in them)
def sieve(n):
  primes = []
  sieve = [False]*n
  for i in range(2, n):
    if sieve[i]:
      continue
    primes.append(i)
    for j in range(i*i,n,i):
      sieve[j] = True
  return primes

# Find all "potential" primes under 1000000 (only 3,5,7,9's allowed)
primes = set(sieve(1000000))
potential_primes = []
for num in primes:
  digits = set(int(i) for i in str(num))
  if not digits & illegal_digits:
    potential_primes.append(num)

def is_circular(n):
  s = str(n)
  for _ in range(len(s)):
    if int(s) not in potential_primes:
      return False
    s = s[1:]+s[0] # Rotate
  return True

# Check all potential primes
ans = 2 # Account for 2 and 5, which contain "illegal digits"
for num in potential_primes:
  if is_circular(num):
    ans += 1

print(ans)
