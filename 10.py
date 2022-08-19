n = 2000000

sieve = [False]*n
ans = 0
for i in range(2,n):
  if sieve[i]:
    continue
  ans += i
  for j in range(i*i, n, i):
    sieve[j] = True

print(ans)
