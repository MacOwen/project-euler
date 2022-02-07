def reverse(x):
    ans = 0
    while x:
        ans *= 10
        ans += x%10
        x//=10
    return ans

def is_palindrome(x):
    return x == reverse(x)

def largest_palindrome():
    largest = 0
    for a in range(999,99,-1):
        for b in range(999,99,-1):
            if is_palindrome(a*b):
               largest = max(largest, a*b)
    return largest

print(f"Result: {largest_palindrome()}")
