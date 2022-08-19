import math

# math.lcm works in python3.10
def lcm(x,y):
  return (x*y)//math.gcd(x,y)

ans=1
for i in range(1,21):
  ans = lcm(ans,i)

print(ans)
