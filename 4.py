def is_palindrome(n):
  return str(n) == str(n)[::-1]

ans = 0

for i in range(100,1000):
  for j in range(100,1000):
    if is_palindrome(i*j):
      ans = max(ans, i*j)

print(ans)
