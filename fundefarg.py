def log_entero(num, base=2):
    cont = 0
    while num >= base:
        cont+=1
        num /= base
    return cont
print(log_entero(1024))
print(log_entero(1000,10))
print(log_entero(9,3))
