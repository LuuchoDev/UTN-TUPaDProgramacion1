def suma_digitos(num):
    if num < 10:
        return num
    else:
        return num % 10 + suma_digitos(num // 10)

num_usuario = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(num_usuario)
print(f"La suma de los dígitos de {num_usuario} es: {resultado}")