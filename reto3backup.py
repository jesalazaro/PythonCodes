def func(text):
    counter = 1
    endvalues = []


    for i in range(len(text) - 1):
        if text[i + 1] == text[i]:
            counter += 1
            #print(text[i+1])
            #print(counter)

        else:
            endvalues.append(counter)
            counter = 1

    endvalues.append(counter) #adds the final counter value


    newlist = []
    newlist.append(text [0])
    for i, element in enumerate(text):
        if i > 0 and text[i - 1] != element:
            newlist.append(element)


    return(newlist, endvalues)


#x = func([" A"," A"," A"," B"," B"," A"," C"," C"])

#x = [" A"," A"," A"," B"," B"," A"," C"," C"]

z = list(input("ingrese los valores"))

x, y = func(z)

print(x)
print(y)
