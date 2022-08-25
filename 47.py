import math

# Given an integer n, return the numbers of distinct prime factors
def num_prime_factors(n):
  ans=0
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      ans += 1
      while n%i==0:
        n//=i
  if n>1:
    ans += 1
  return ans

# Brute-force linear search, stop at first sequence of 4 numbers with 4 prime factors
i=4
a = b = c = d = False
ans = 0
while True:
  a,b,c = b,c,d
  d = num_prime_factors(i)==4
  if a and b and c and d:
    ans = i-3
    break
  i += 1

print(ans)
