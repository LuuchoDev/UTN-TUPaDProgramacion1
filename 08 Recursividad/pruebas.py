def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

num_usuario = int(input("Ingrese un número para calcular la potencia: "))
base = int(input("Ingrese la base: "))
resultado = potencia_recursiva(base, num_usuario)
print(f"{base} elevado a la {num_usuario} es: {resultado}")
