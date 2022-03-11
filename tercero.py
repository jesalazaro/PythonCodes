def stepCounter(positions):

    counter = 0
    calculatedStepX = 0
    calculatedStepY = 0
    k = 0
    j = 0

    for i in positions:

        #genera el paso para las cordenadas x,y
        calculatedStepX = abs(i[0] - j) 
        j = i[0]
    
        calculatedStepY = abs(i[1] - k)      
        k = i[1]

        #print(calculatedStepX)
        #print(calculatedStepY)
        
        """
        debido a que el paso para movimientos mayores  a 1,1 se tienen que tratar de manera
        que un movimiento de 2,2 a 4,5 es como tal tres movimientos uno a 3,3 otro a 4,4 y uno de 4,5
        las siguientes instrucciones calculan cual de los dos pasos x o y es mayor
        se suma un paso por avance continuo x,y y luego se suma el resto de los pasos ya sean x o y
        """
        if  calculatedStepX > 1 and calculatedStepY > 1:
            
            if calculatedStepX > calculatedStepY:
                
                susbstraction = calculatedStepX - calculatedStepY
                i = 0
                while i < calculatedStepY:
                    counter += 1
                    i += 1
                j = 0
                while j < susbstraction:
                    j += 1
                    counter += 1


            if calculatedStepY > calculatedStepX:
                
                susbstraction = calculatedStepY - calculatedStepX
                i = 0
                while i < calculatedStepX:
                    counter += 1
                    i += 1
                j = 0
                while j < susbstraction:
                    j += 1
                    counter += 1
        
        # si el movimiento es diagonal en ambas direcciones se suma uno al contador

        elif calculatedStepX == calculatedStepY:
            counter += calculatedStepX
        
        #si el movimiento es solo en x se suma al contador

        elif calculatedStepX > 0 and calculatedStepX != calculatedStepY and calculatedStepX > calculatedStepY:
            counter += calculatedStepX
        
        #si el movimiento es solo en y se suma al contador

        elif calculatedStepY > 0 and calculatedStepY != calculatedStepX :
            counter += calculatedStepY

    return counter
 


arrayExp = [(0,0),(1,1),(1,3)]
#arrayExp = [(0,0),(1,2),(3,3)]
#arrayExp = [(0,0),(4,5)]
print(stepCounter(arrayExp))