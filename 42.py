content = open('files/p042_words.txt').read()
words = [i[1:-1] for i in content.split(',')]

# Maximum possible ASCII sum based on given words
max_triangle = len(max(words, key=lambda x:len(x)))*26

# Create a set of all possible triangle numbers
triangles = [1]
i = 2
while triangles[-1]+i <= max_triangle:
  triangles.append(triangles[-1]+i)
  i += 1
triangles = set(triangles)

# Iterate through all words, counting how many correspond to triangle numbers
ans = 0
for s in words:
  ascii_sum = sum(ord(c)-ord('A')+1 for c in s)
  if ascii_sum in triangles:
    ans += 1

print(ans)
