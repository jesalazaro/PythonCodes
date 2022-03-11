def potencia(b,  n):
    if n == 0:
        return 1
    else:
        return potencia(b, n-1) * b


print(potencia(4,2))
