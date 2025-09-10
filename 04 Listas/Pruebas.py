datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = []

## Crea una nueva lista sin elementos repetidos
for num in datos:
    if num not in datos_sin_repetidos:
        datos_sin_repetidos.append(num)
    else:
        continue

print(datos_sin_repetidos)