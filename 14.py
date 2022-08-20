dp = {}

def collatz(x):
  if x == 1:
    return 1
  if x in dp:
    return dp[x]

  if x%2==0:
    y = x//2
  else:
    y = x*3+1

  ans = collatz(y)+1
  dp[x] = ans
  return ans

ans = 0
high = 0
for i in range(1,1000001):
  cur = collatz(i)
  if cur > high:
    high = cur
    ans = i

print(ans)
