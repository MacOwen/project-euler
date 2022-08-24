def get_nth_digit(n):
  n -= 1 # Account for 0-indexing
  # Split numbers into sequences based on their # of digits (lengths 9, 90, 900, ...)
  sequence_length = 9
  digits = 1
  while n > sequence_length*digits:
    n -= sequence_length*digits
    sequence_length *= 10
    digits += 1
  # Find remainder and get correct digit in sequence
  m = n % digits
  n //= digits
  return int(str(10**(digits-1)+n)[m])

# Find product of n'th digits for powers of 10
ans = 1
for i in range(7):
  ans *= get_nth_digit(10**i)

print(ans)
