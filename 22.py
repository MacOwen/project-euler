s = open("files/p022_names.txt").read()
names = [i[1:-1] for i in s.split(',')]

names.sort()
ans = 0
for i,name in enumerate(names):
  ans += (i+1)*sum([ord(c)-ord('A')+1 for c in name])

print(ans)
