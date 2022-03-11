def division(a, b):
    try:
        coc = a//b
        res = a % b
        return(coc, res)
    except:
        print("Error en la división de", a, "entre", b)
def main():
    num = int(input("digite el dividendo:"))
    div = int(input("digite el divisor:"))
    print(division(num, div))
main()
