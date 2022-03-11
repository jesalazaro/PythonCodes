import json

count = 0

user_products = []

dicpro = dict()
user_input = input("ingrese nombre y llave de cada producto: ")
temp = user_input.split( )

for i in range(len(user_input)):
    word = user_input.split(",")

for x, y in zip(*[iter(word)]*2):
    key = x
    value = int(y)
    dicpro[key] = value


print(dicpro)

with open("json/market.json" , "w") as write_file:
    json.dump(dicpro, write_file)


with open("json/market.json", "r") as read_file:
    data = json.load(read_file)

prod = input("productos: ")
products = []

print(data)

for i in prod.split():
    products.append(i)


for i in products:
    count += data[i]
    user_products.append(i)

print(count)
print(user_products)
