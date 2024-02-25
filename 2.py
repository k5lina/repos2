def f(n):
    k = 1
    a = 0
    while k < n:
        k *= 2
        a += 1
    return a

print(f(int(input())))
