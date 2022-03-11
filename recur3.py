def f(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return f(n-2)

print(f(9))
