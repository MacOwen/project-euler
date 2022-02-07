sum_of_squares = 0
for i in range(1,101):
    sum_of_squares += i*i

square_of_sums = (100*(101))//2
square_of_sums *= square_of_sums

print(f"Result: {square_of_sums-sum_of_squares}")
