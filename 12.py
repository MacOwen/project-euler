import math

def num_divisors(n):
  ans = 0
  for i in range(1,math.ceil(math.sqrt(n))):
    if n%i==0:
      ans += 2
  if int(math.sqrt(n))**2 == n:
    ans+=1
  return ans

k = 1
while True:
  x = (k*(k+1))//2
  if num_divisors(x) > 500:
    print(x)
    break
  k += 1
