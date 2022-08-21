# Get all primes < N
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

# Determine if the decimal notation of a prime N will repeat indefinitely
def decimal_repeats(n):
  while n%2==0:
    n //= 2
  while n%5==0:
    n //= 5
  return n != 1


primes = sieve(1000)

# For each prime, find the repeating factor
# We know that prime reciprocals do not have any non-repeating decimal digits
# A rational number's decimal expansion will eventually terminate or predictably repeat

best = 0
ans = 0

for prime in primes:
  if not decimal_repeats(prime):
    continue
  x = 9
  num_digits = 1
  while x%prime != 0:
    x *= 10
    x += 9
    num_digits += 1
  if num_digits > best:
    best = num_digits
    ans = prime

print(ans)
