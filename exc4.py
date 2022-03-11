try:
    num = int(input("Ingrese un número: "))
    re = 100/num # generar excepción se si digitó o
    print(re)
except Exception as e:
    print(e, "\n", type(e))
