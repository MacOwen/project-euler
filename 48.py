# Return the result of (x^y)%m
def modpow(x,y,m):
  if y==0:
    return 1
  if y%2==0:
    ans = modpow(x,y//2,m)
    return (ans*ans)%m
  else:
    ans = modpow(x,y-1,m)
    return (x*ans)%m

# Find the result of 1^1+2^2+3^3+...+1000^1000 (mod 10^10)
ans = 0
for i in range(1,1001):
  ans += modpow(i,i,10**10)
ans %= 10**10

print(ans)
