def sum(number1, number2):

    array1 = [int(x) for x in str(number1)] #Pasa los digitos del primer número a un array
    array1Reversed = []
    for i in reversed(array1):
        array1Reversed.append(i)    #Genera el reverso del array1
    print(array1Reversed)

    array2 = [int(y) for y in str(number2)] #lo mismo para el número 2
    array2Reversed = []
    for i in reversed(array2):
        array2Reversed.append(i)
    print(array2Reversed)

    f_len = len(array1Reversed)-(len(array2Reversed) - 1) # se suman los números uno a uno
    for i in range(0, len(array2Reversed), 1):
        if f_len - i >= len(array1Reversed):
            break
        else:
            array1Reversed[i] = array1Reversed[i] + array2Reversed[i]
    return array1Reversed

print(sum(153,34))