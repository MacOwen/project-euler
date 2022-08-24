import math

# Array mapping perimeter value to # of valid ways
p = [0]*1001

# Go through all possible a and b values, check for valid c and increment their corresponding perimiter score
for a in range(1,501):
  for b in range(1,501):
    c = math.sqrt(a*a+b*b)
    if math.floor(c) == math.ceil(c):
      c = int(c)
      if a+b+c > 1000:
        continue
      p[a+b+c] += 1

ans = p.index(max(p)) # Find p-value with greatest number of solutions

print(ans)
