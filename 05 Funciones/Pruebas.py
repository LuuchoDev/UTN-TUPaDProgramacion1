def calcular_promedio(a, b, c):
    ## Esta función calcula el promedio de tres números.
    promedio = (a + b + c) / 3
    return promedio
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
print(f"El promedio de {num1}, {num2} y {num3} es {calcular_promedio(num1, num2, num3)}")