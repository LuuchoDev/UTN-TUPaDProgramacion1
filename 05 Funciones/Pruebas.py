def operaciones_basicas(a, b):
    ## Realiza las operaciones básicas entre dos números y devuelve los resultados.
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}")