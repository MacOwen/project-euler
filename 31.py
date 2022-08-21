coins = [1,2,5,10,20,50,100,200]

dp = [0]*201
dp[0] = 1

# Solve DP iteratively
for c in coins:
  for i in range(201):
    if i+c>200:
      continue
    dp[i+c] += dp[i]

print(dp[-1])
