"""
def order(travels, initialAirport):
    l = []
    l.append(initialAirport)
    for i in range(len(travels)):
        for i,k in travels:
            if i == initialAirport:
                l.append(k)
                initialAirport = k
    return l
"""
def order(travels, initialAirport):
    travel_list = []
    first = initialAirport  # se coloca el aeropuerto inicial
    
    for j in range(len(travels)): #ciclo para cada aeropuerto
        airports = []
        travel_list.append(first) # se coloca el primer aeropuerto en la lista

        for i, k in travels:
            if i == first:   #si el aeropuerto esta se añade el segundo valor de la tupla a la lista
                airports.append(k)

        if airports == []:   #si la lista sigue vacia es que no se encontro un aeropuerto por tal razón break 
            break
        
        orderk = min(airports) # orden alfabetico

        travels.remove((first, orderk)) #se remueve el aeropuerto de la lista inicial dado que esto daria problemas
        first = orderk #el segundo valor de la tupla se vuelve el primer aeropuerto

    travel_list.append(first) #se anexa el valor a la lista, luego se repiet el ciclo hasta que la lista inicial queda vacia

    if travels == []:  #cuando la lista esta vacia se retorna la lista ordenada
        
        return travel_list

    return None #en caso de que no cumpla se retorna none

travels = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
initialAirport = 'YUL'

#travels = ([('SFO', 'COM'), ('COM', 'YYZ')])
#initialAirport = 'COM'

#travels =  [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
#initialAirport = 'A'

print(order(travels, initialAirport))
