ans = 1
num = 1
step = 2
# Expand 500 layers out from the center
for i in range(500):
  # Each corner is an odd number, the spacing increases by 1 every layer
  ans += num*4 + step*10 # (num+step)+(num+2*step)+...
  num += step*4
  step += 2

print(ans)
