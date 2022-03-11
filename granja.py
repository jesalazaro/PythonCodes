def vacas(x,y):
    #ecuacion para los litros de leche en base a los metros cuadrados y al número de vacas por semana (7)
    l = 7*x*y
    return l


def gallinas(d):

    # número de gallinas

    d = int(c/3)

    print("número de gallinas", d)

    #huevos cada 3 dias

    e = d/2*(30/3)

    print("huevos de 3 dias ", e)

    #huevos cada 5 dias

    f = d/2*(30/5)

    print("huevos de 5 dias ", f)

    return e , f


a = int(input("numero de vacas:  "))
b = int(input("metros cuadrados que requiere cada vaca:  "))

print(vacas(a,b))

c = int(input("número de aves: "))

print(gallinas(c))


#cantidad de escorpiones pequeños

d = int(input("cantidad de escorpiones pequeños"))
e = int(input("cantidad de escorpiones medianos"))
f = int(input("cantidad de escorpiones grandes"))

#masa de los escorpiones pequeños
g = d*20
#masa de los escorpiones medianos
h = e*30
#masa de los escorpiones grandes
i = f*50

poblacion = (d + e + f)*2/3
