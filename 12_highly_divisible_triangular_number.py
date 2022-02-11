import math

def num_factors(x):
    ans = 0
    for i in range(1,int(math.sqrt(x))):
        if x%i == 0:
            ans += 2
    if int(math.sqrt(x))**2 == x:
        ans += 1
    return ans

factors = 0
triangle = 0
inc = 1
while factors <= 500:
    triangle += inc
    inc += 1
    factors = num_factors(triangle)

print(triangle)
