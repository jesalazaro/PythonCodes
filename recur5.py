def fibonacci(n,m):
    if m == 0:
        return n
    else:
        return fibonacci(n+n+1,m-12)

print(fibonacci(1,12))
