def func_filtrar_productos(list):
    aa = []
    for i in list:
        if i not in aa:
            aa.append(i)
    return aa
#list = ["mancuernas", "pesas", "barras", "bicicleta", "patineta", "ruedas", "mancuernas", "ruedas", "raquetas", "ruedas","bicicleta"]
#list = [16, 14, 13, 5, 2, 9, 17, 14, 15, 5, 4, 4, 15, 7, 15, 16, 2, 2]
#print(func_filtrar_productos(list))

def func_productos_faltantes(posiciones, faltantes, elemento):
    b = []
    for  i in posiciones:
        if faltantes[i] == elemento:
            b.append(i)
    return b


#posiciones = [0,3,5,2,1,9,6,8,10]
#faltantes = ["mancuernas", "pesas", "barras", "bicicleta", "patineta", "ruedas", "mancuernas", "ruedas", "raquetas", "ruedas", "bicicleta"]
#elemento = "ruedas"

#print(func_productos_faltantes(posiciones, faltantes, elemento))

def func_encontrar_faltantes(l_sobrantes_otros, l_mis_productos):

    cc = []

    for i in l_sobrante_otros:
        if i not in l_mis_productos:
            cc.append(i)
    return cc

l_sobrante_otros = ["mancuernas", "pesas", "barras", "bicicleta", "patineta", "multifuerza", "pelotas", "raquetas"]
#
l_mis_productos = ["ruedas", "mancuernas", "raquetas", "bicicleta"]
#
print(func_encontrar_faltantes(l_sobrante_otros, l_mis_productos))

def func_obtener_intercambiables(l_sobrantes_otros, l_sobrantes_mios):

    dd = []
    counter1 = 0
    counter2 = 0

    for i in l_sobrantes_otros:
        if i in l_sobrantes_mios:
            a = 1
        else :
            counter1 += 1



    for j in l_sobrantes_mios:
        if j in l_sobrantes_otros:
            a = 1
        else :
            counter2 += 1


    if counter1 < counter2:
        return counter1

    if counter2 < counter1:
        return counter2

    if counter1 == counter2:
        return counter1


#l_sobrantes_mios = [10, 0, 9, 3, 2, 4]
#l_sobrantes_otros = ["mancuernas", "pesas", "barras", "bicicleta", "patineta", "multifuerza", "pelotas", "raquetas"]
#
#l_sobrantes_mios = ["ruedas", "mancuernas", "raquetas", "bicicleta", "gorras", "gafas", "cascos"]
#
#print(func_obtener_intercambiables(l_sobrantes_otros, l_sobrantes_mios))
