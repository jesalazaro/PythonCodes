
x = int(input("ingrese el número de canciones: "))

x = int(input("ingrese el número de canciones: "))

#número de coristas
y = 2*x + 4

#número de musicos
z = int((y + x)/5)

print(x, y , z)

if ( 0 <= z <= 20):

    print("uno")

elif ( 21 <= z <= 30):

    print("dos")

elif( 31 <= z <= 50):

    print("tres")

elif( z > 50):

    print("cuatro")
