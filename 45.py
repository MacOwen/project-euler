import math

"""
An integer x cannot qualify as Tn,Pn, and Hn unless:
  8x+1 is a square
  24x+1 is a square
These solutions can be iterated through quicker by iterating through squares and checking %8 and %24

After finding all potential numbers (that satisfy the %8 %24 condition), find all valid solutions among them
"""

# Obtain all valid potential numbers, using the first n square numbers
def get_valid_indices(n):
  # Find triangle numbers that equal 1 (mod 8)
  triangular = set()
  for i in range(1,n+1):
    if (i*i)%8==1:
      orig = (i*i-1)//8
      triangular.add(orig)
  # Find pentagonal numbers that equal 1 (mod 24), and that match the previous condition
  ans = []
  for i in range(1,n+1):
    if (i*i)%24==1:
      orig = (i*i-1)//24
      if orig in triangular:
        ans.append(orig)
  return ans

indices = get_valid_indices(1000000)

ans = 0
for i in indices:
  x = int(math.sqrt(1+8*i))
  y = int(math.sqrt(1+24*i))
  if x%4==3 and y%6==5 and i != 1 and i != 40755:
    ans = i
    break

print(ans)
