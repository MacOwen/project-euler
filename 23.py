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

# Find the set of all abundant numbers < 28123
abundant = set()
for i in range(28123):
  if d(i) > i:
    abundant.add(i)

# Determine if n can be constructed as the sum of two abundant numbers
def possible(n):
  for a in abundant:
    if a > n:
      break
    b = n-a
    if b in abundant:
      return True
  return False

# Find all numbers which cannot be constructed as the sum of two abundant numbers
ans = 0
for i in range(28123):
  if not possible(i):
    ans += i

print(ans)
