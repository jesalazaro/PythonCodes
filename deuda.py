om#valor de la deuda
a = int(input("valor de la deuda: "))

b = int(input("valor del interes diario 10, 20, 30, 40, etc porciento: "))

c = int(input("número de dias: "))

tipo = input("tipo de ingreso, simple o compuesto (escriba una opción)")

#conversion de porcentaje a decimal
conv = b/100

if tipo == 'simple':
    simple = float(a*conv*c) + a
    print("el valor de la deuda es: ", simple)
elif tipo == 'compuesto':
    compuesto = float(a*(1+conv)**5) + a
    print("el valor de la deuda es: ", compuesto)

else :
    print("no es una opcion valida")
