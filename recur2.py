def buscar_parcial(str, ch, n):
    if n > 0:
        return (str[n-1] == ch) or buscar_parcial(str, ch, n-1)
    else:
        return False

def buscar(str,ch):
    return buscar_parcial(str,ch,len(str))

print(buscar("Hola mundo", "d"))
