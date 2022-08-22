"""
Upper of D digits when D(9!) < all D-digit numbers
"""

factorial_map = [1]*10
for i in range(1,10):
  factorial_map[i] = factorial_map[i-1]*i

# Find maximum D for which d-digit numbers can never be curious
def get_limit():
  d = 1
  while d*factorial_map[9] >= 10**(d-1):
    d += 1
  return d-1

# Determine if an integer N is curious
def is_curious(n):
  return n == sum(factorial_map[int(i)] for i in str(n))

# Test all possible curious numbers
ans = 0
high = get_limit()
for i in range(3,10**(high-1)):
  if is_curious(i):
    ans += i

print(ans)
