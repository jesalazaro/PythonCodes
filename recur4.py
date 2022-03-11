def g(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return g(n-3 )

print(g(10))
print(g(9))
print(g(11))
print(g(12))
print(g(15))
