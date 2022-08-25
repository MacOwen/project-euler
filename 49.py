# Return all primes < n
def sieve(n):
  primes = []
  sieve = [False]*n
  for i in range(2,n):
    if sieve[i]:
      continue
    if len(str(i))==4:
      primes.append(i)
    for j in range(i*i,n,i):
      sieve[j] = True
  return primes

# Get all 4-digit primes
primes = set(sieve(10000))

def is_permutation_sequence(a,b,c):
  return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

# Iterate through every possible arithmetic prime sequence
ans = 0
for a in primes:
  for inc in range(1,(10000-a)//2):
    b = a+inc
    c = a+inc*2
    if b in primes and c in primes and is_permutation_sequence(a,b,c) and a != 1487:
      ans = str(a)+str(b)+str(c)

print(ans)
