# Create a set of the first 2500 pentagonal numbers
pent = []
for i in range(1,2501):
  pent.append((i*(3*i-1))//2)
pent = set(pent)

# Check for solution for Pj,Pk within the first 2500 pentagonal numbers
ans = 1<<64 # 2^64 for large initial number
for j in range(1,2501):
  for k in range(j+1,2501):
    pj = (j*(3*j-1))//2
    pk = (k*(3*k-1))//2
    if pj+pk in pent and pk-pj in pent:
      ans = min(ans, pk-pj)

print(ans)
