def numberTen(number):
    count = 0
    for i in range(99999999999999999999999): #se genera un rango muy grande para que el codigo genere la mayor cantidad de números
        sum = 0
        n = i
        while (i != 0):  #Instrucciónes para calcular los números en los cuales los digitos sumados den 10
            sum = sum + int(i % 10)
            i = int(i/10)
        if sum == 10:  #si el resultado de la suma de los digitos es 10 devuelve el número
            count += 1
            if count == number:
                print("the result is ", n)
                return n

numberTen(7)