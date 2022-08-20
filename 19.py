months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ans=0

year = 1901
day = 2
for i in range(100):
  if year%4==0:
    months[1] = 29
  else:
    months[1] = 28
  for m in months:
    if day == 0:
      ans += 1
    day += m
    day %= 7

print(ans)
