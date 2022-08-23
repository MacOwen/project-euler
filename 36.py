def to_binary(n):
  s = ''
  while n:
    if n&1:
      s += '1'
    else:
      s += '0'
    n >>= 1
  return s[::-1]

# Bruteforce all numbers < 10^6
ans = 0
for i in range(1,1000000):
  a = str(i)
  b = to_binary(i)
  if a == a[::-1] and b == b[::-1]:
    ans += i

print(ans)
