def division(a, b):
    if b == 0:
        raise ValueError("!Error de división por cero¡")
    else:
        coc = a//b
        res = a%b
        return(coc, res)
try:
    print(division(10, 0))
