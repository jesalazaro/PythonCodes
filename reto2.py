PRR1 = input("Cadena de caracteres del primer producto: ")
PRR2 = input("Cadena de caracterese del segundo producto: ")
PRCAD = input("Cadena de caracteristicas del día: ")


PR1 = []
PR11 = []
PR2 = []
PR22 = []

end = ""

counter1 = 0
counter2 = 0

for letra in PRR1:
    PR11.extend(letra)

PR1 = list(set(PR11))

for letra in PRR2:
    PR22.extend(letra)

PR2 = list(set(PR22))

for i in PRCAD:

    for j in PR1:
        if i == j:
            counter1 += 1
    for k in PR2:
        if i == k:
            counter2 += 1

    if counter1 > counter2:

        end = end + "J"

    if counter1 < counter2:

        end = end + "K"

    if counter1 == counter2:
        end = end + "L"
    print(counter1, counter2)


print(end)
