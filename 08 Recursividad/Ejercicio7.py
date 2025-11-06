def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("Ingrese el número de bloques en el nivel inferior: "))
print(f"Total de bloques: {contar_bloques(niveles)}")