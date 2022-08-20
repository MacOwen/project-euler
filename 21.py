import math

dp = {}
def d(n):
  if n in dp:
    return dp[n]
  ans = 0
  for i in range(1, int(math.sqrt(n))+1):
    if n%i==0:
      ans += i
      if i != n//i and n//i < n:
        ans += n//i
  dp[n] = ans
  return ans

ans = 0
for i in range(10000):
  if i == d(d(i)) and i != d(i):
    ans += i

print(ans)
