def variable_argument(var1, *vari):
    print("salida:"+ str(var1))
    for var in vari:
        print(var)

variable_argument(60)
variable_argument(100, 90, 67, 23, 10)
