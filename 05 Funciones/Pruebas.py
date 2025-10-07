
def tabla_multiplicar(numero):
    ## Imprime la tabla de multiplicar del número dado
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)