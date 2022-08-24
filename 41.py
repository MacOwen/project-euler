import math
import itertools

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True

# For each n value, iterate over all permutations of [1,2,3,..,n], testing for primality
ans = 0
for num_digits in range(1,10):
  s = [str(i) for i in range(1,num_digits+1)]
  for p in itertools.permutations(s):
    num = int(''.join(p))
    if is_prime(num):
      ans = max(ans, num)

print(ans)
