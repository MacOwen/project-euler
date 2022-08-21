power_map = [i**5 for i in range(10)]

def power_sum(n):
  return sum(power_map[int(j)] for j in str(i))

# Find the first power of 10 for which a sum of 5th powers will always be smaller
def find_limit():
  digits = 1
  num = 1
  while (digits+1)*power_map[9] >= num:
    num *= 10
    digits += 1
  return num

# Find the limit L
limit = find_limit() # All possible answers are within the range (1,L)

# Test all potential numbers under limit, and add valid numbers to the solution
ans = 0
i = 2
while i < limit:
  num = power_sum(i)
  # If number exceeds target, skip to next multiple of 10
  if num == i:
    ans += i
  i += 1

print(ans)
