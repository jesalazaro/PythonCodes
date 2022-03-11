from pprint import pprint
def informar(**var):
    pprint(var)
    for key, value in var.items():s
        pprint("%s == %s" %(key, value))


informar(nombre="Poseidon", edad = "6000", ciudad = "Olimpo")
