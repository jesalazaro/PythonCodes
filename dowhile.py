def min_maquina():
    Xi = 1.0
    bandera = True

    while(bandera or Xi > 0.0):
        bandera = False

        Xo = Xi
        Xi = Xo/2.0
    return Xo

print("el minimo numero positivo", end = "")
print("en esta maquina es: ", min_maquina())
