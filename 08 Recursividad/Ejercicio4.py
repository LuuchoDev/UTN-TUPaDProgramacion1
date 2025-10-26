def decimal_a_binario_recursivo(n):
    if n == 0:
        return ""
    else:
        cociente = n // 2
        resto = n % 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

num_usuario = int(input("Ingrese un número decimal para convertir a binario: "))
if num_usuario < 0:
    print("Por favor, ingrese un número positivo.")
elif num_usuario == 0:
    print("El número 0 en binario es: 0")
else:
    binario = decimal_a_binario_recursivo(num_usuario)
    print(f"El número {num_usuario} en binario es: {binario}")