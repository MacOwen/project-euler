def f(x):
    prev = 1
    cur = 1
    s = 0 # Sum of even values
    while cur < x:
        val = prev+cur
        if val % 2 == 0:
            s += val
        prev = cur
        cur = val
    return s

print(f"Result: {f(4000000)}")
