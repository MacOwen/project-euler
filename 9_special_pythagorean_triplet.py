# Iterate through all pairs of a and b
# The value of c can be found instantly since a, b, and c must sum to 1000
def triplet_product(x):
    for a in range(1,x):
        for b in range(a+1,x):
            c = 1000-a-b
            if a*a + b*b == c*c:
                return a*b*c
    return -1

print(f"Result: {triplet_product(1000)}")
