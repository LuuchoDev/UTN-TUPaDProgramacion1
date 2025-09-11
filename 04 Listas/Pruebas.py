notas = [
    [8, 7, 9],   # Estudiante 1
    [6, 5, 7],   # Estudiante 2
    [9, 8, 10],  # Estudiante 3
    [7, 6, 8],   # Estudiante 4
    [10, 9, 9]   # Estudiante 5
]

## Calcula y muestra el promedio de cada estudiante
for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    print(f"El promedio del estudiante {i+1} es: {promedio}.")
    
## Calcula y muestra el promedio de cada materia
for j in range(3):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedio = suma / len(notas)
    print(f"El promedio de la materia {j+1} es: {promedio:.2f}.")