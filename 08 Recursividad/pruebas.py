def factorial_recursivo(x):
    if x == 1:
        return 1
    else:
        return x * factorial_recursivo(x - 1)

num_usuario = int(input("Ingrese un número para calcular su factorial: "))

for i in range (1, num_usuario + 1):
    resultado = factorial_recursivo(i)
    print(f"El factorial de {i} es: {resultado}")
