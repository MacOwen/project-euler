# Number stored in least-significant digit form
digits = [0]*500

# Double number stored in array
def double():
    carry = 0
    for i in range(500):
        digits[i] = digits[i]*2 + carry
        carry = digits[i]//10
        digits[i] %= 10

# Starting at 1, double number 1000 times
digits[0] = 1
for _ in range(1000):
    double()

# Print the sum of digits array
print(sum(digits))
