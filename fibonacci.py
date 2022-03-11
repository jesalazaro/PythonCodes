def funcCacularSerieFibonnaci(cantidad):
    a = 0
    b = 1
    c = 0
    result = []
    for i in range(cantidad):
        result.append(c)
        a = b 
        b = c
        c = a + b
    print(result)
    return result

resultado = funcCacularSerieFibonnaci(20)