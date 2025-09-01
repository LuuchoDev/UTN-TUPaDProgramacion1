

num = int(input("Ingrese un número: "))
numInvertido = 0
while num > 0:
    digito = num % 10
    numInvertido = numInvertido * 10 + digito
    num = num // 10
print(f"El número invertido es: {numInvertido}")
