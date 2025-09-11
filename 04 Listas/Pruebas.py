temperaturas = [
    [10, 20],
    [12, 22],
    [8, 18],
    [11, 21],
    [9, 19],
    [13, 23],
    [7, 17]
]
## calcular el promedio de las minimas y maximas
minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)
print(f'Promedio de temperaturas mínimas: {promedio_minimas}')
print(f'Promedio de temperaturas máximas: {promedio_maximas}')