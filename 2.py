a=0
b=1
ans=0

while a < 4000000:
  a,b = b,a+b
  if a%2==0:
    ans += a

print(ans)
