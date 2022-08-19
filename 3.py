import math

n = 600851475143
sq = math.ceil(math.sqrt(n))
ans = 0
for i in range(2,sq+1):
  if n%i==0:
    ans = i
    while n%i==0:
      n /= i

print(ans)
