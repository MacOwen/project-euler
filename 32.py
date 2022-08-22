import math

"""
Only 1x4 and 2x3 products will work (all other configurations result in too few/many total digits)
"""

ans = 0
valid_products = set() # Use set to prevent counting the same product multiple times

# Solve all 1x4 solutions
for a in range(1,10):
  for b in range(1234, 9877): # 1234 lowest, 9876 highest
    c = a*b
    if len(str(a)+str(b)+str(c)) != 9:
      continue
    digits = set(list(str(a))+list(str(b))+list(str(c)))
    digits.add('0') # Add 0 to test for 10 digits (prevents 0 from counting towards 9-digit goal)
    if len(digits) == 10 and c not in valid_products:
      valid_products.add(c)
      ans += c

# Solve all 2x3 solutions
for a in range(12,99):
  if a%10==a//10 or a%10==0:
    continue
  for b in range(123,988): # 123 lowest, 987 highest
    c = a*b
    if len(str(a)+str(b)+str(c)) != 9:
      continue
    digits = set(list(str(a))+list(str(b))+list(str(c)))
    digits.add('0') # Add 0 to test for 10 digits (prevents 0 from counting towards 9-digit goal)
    if len(digits) == 10 and c not in valid_products:
      valid_products.add(c)
      ans += c

print(ans)
