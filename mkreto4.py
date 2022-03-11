import json

count = 0

user_products = []

with open("json/market.json", "w") as f:
    pr = input("ingrese los valores para el json")
    f.write(pr)


with open("json/market.json", "r") as read_file:
    data = json.load(read_file)

prod = input("productos: ")
products = []


for i in prod.split():
    products.append(i)


for i in products:
    try:
        count += data[i]
        user_products.append(i)
    except Exception:
        pass


print(count)
print(user_products)
