def division(a, b):

    try:
        coc = a // b
        rest = a % b
        return(coc, res)
    except:
        print("Error en la división de", a , "entre", b)
        return ""

print(division(10, 0))
print(division(1024, 10))
