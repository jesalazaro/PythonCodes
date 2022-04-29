#Ejercicio en python usando random

import random 

myArray = []
a = 0 
for i in range(10):
	a = random.randint(0,10)
	myArray.append(a)

c = 0 

for i in myArray:
	print(i)
	c += 1

if (c < 50):
	print("Eureka")

else print("Este es el ultimo taller") 