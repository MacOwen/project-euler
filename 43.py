import itertools

primes = [2,3,5,7,11,13,17]
num = '0123456789'

# Given integer string of length 10, find if it matches the specific property
def is_divisible(s):
  for i in range(7):
    if int(s[i+1:i+4])%primes[i] != 0:
      return False
  return True

# Go through all possible 0-9 pandigital numbers with the special property
ans = 0
for p in itertools.permutations(num):
  if p[0] == '0':
    continue
  s = ''.join(p)
  if is_divisible(s):
    ans += int(s)

print(ans)
