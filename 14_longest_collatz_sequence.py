lengths = [0]*1000001
lengths[1] = 1

# Explore all values under 1,000,000
for i in range(2,1000001):
    # Calculate collatz sequence until previously calculated value is found
    chain = [i]
    while chain[-1] > 1000000 or lengths[chain[-1]] == 0:
        if chain[-1]%2 == 0:
            chain.append(chain[-1]//2)
        else:
            chain.append(chain[-1]*3+1)
    # Fill length values for all numbers in collatz sequence
    l = lengths[chain[-1]]-1
    while chain:
        l += 1
        num = chain.pop()
        if num > 1000000:
            continue
        lengths[num] = l

# Find starting number with longest collatz sequence
longest = 0
longest_idx = 0
for i in range(1,1000001):
    if lengths[i] > longest:
        longest = lengths[i]
        longest_idx = i

print(longest_idx)
