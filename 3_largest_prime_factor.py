def largest_prime_factor(x):
    for i in range(2,x):
        while x % i == 0:
            x /= i
        if x == 1:
            return i

print(f"Result: {largest_prime_factor(600851475143)}")
