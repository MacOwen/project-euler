import math

def is_curious(a,b):
  if a%10 == 0 or b%10 == 0:
    return False
  g = math.gcd(a,b)
  if g == 1:
    return False
  if a//g >= 10 or b//g >= 10:
    return False
  # Try eliminating all 4 possible pairs of digits
  for i in range(2):
    for j in range(2):
      a_remove = int(str(a)[i])
      b_remove = int(str(b)[j])
      a_keep = int(str(a)[(i+1)%2])
      b_keep = int(str(b)[(j+1)%2])
      # Crossed digits have to match
      if a_remove != b_remove:
        continue
      # Remaining digits cannot match (no trivial 1/1 fractions)
      if a_keep == b_keep:
        continue
      # Numbers with removed digits match the reduced fraction
      g_keep = math.gcd(a_keep,b_keep)
      if a_keep//g_keep == a//g and b_keep//g_keep == b//g:
        return True
  return False


# Test all possible 2-digit fractions for curiosity
numerator = 1
denominator = 1
for a in range(10,100):
  for b in range(a,100):
    if is_curious(a,b):
      numerator *= a//math.gcd(a,b)
      denominator *= b//math.gcd(a,b)

ans = denominator // math.gcd(numerator,denominator)
print(ans)
