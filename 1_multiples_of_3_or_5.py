def f(x):
    n3 = (x-1)//3 # Num of multiples of 3
    n5 = (x-1)//5 # Num of multiples of 5
    n15 = (x-1)//15 # Num of multiples of 15
    s3 = (n3*(n3+1))//2
    s3 *= 3
    s5 = (n5*(n5+1))//2
    s5 *= 5
    s15 = (n15*(n15+1))//2
    s15 *= 15
    return s3+s5-s15

print(f"Result: {f(1000)}")
