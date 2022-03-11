def sumar_parcial(L,n):
    if n > 0:
        return L[n-1] + sumar_parcial(L, n-1)
    else:
        return 0

def sumar_lista(L):
    return sumar_parcial(L,len(L))

print(sumar_lista([10,11,12,13,14]))
