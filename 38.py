# Find the corresponding pandigital concatenated product for a given integer (0 if none)
def pandigital(num):
  digits = {'0'}
  concat = ''
  n = 1
  while len(concat) < 9:
    s = str(num*n)
    concat += s
    for c in s:
      digits.add(c)
    if len(concat) == 9 and len(digits) == 10 and n > 1:
      return int(concat)
    n += 1
  return 0

# Check all integers < 10^4 for pandigital concatenation
ans = 0
for i in range(1,10000):
  ans = max(ans, pandigital(i))

print(ans)
