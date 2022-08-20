from itertools import permutations

# Find the nth permutation of a list (0-indexed)
def nth_permutation(arr, n):
  ans = []
  while arr:
    # Choose i'th largest number, according to N'th permutation
    fac = 1
    for i in range(1,len(arr)):
      fac *= i
    i = n//fac
    n %= fac
    # Update permutation
    ans.append(arr[i])
    arr.pop(i)
  return ans


digits = [0,1,2,3,4,5,6,7,8,9]

print(''.join(str(i) for i in nth_permutation(digits, 999999)))
