import math

# Golden ratio
phi = (1 + math.sqrt(5))/2

# Use Binet's formula to approximate answer
x = 999+math.log(math.sqrt(5),10)
y = math.log(phi,10)
ans = math.ceil(x/y)

print(ans)
