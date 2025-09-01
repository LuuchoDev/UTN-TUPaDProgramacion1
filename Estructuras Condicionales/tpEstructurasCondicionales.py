## Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

## Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
## Ejercicio 3
num =int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("Por Favor, ingrese un número par.")

## Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres un niño.")
elif (edad >= 12) and (edad < 18):
    print("Eres un adolescente.")
elif (edad >= 18) and (edad < 30):
    print("Eres un adulto joven.")
elif (edad >= 30):
    print("Eres un adulto.")

## Ejercicio 5
contraseña = input("Introduce la contraseña entre 8 y 14 caracteres: ")
if len(contraseña) < 8 or len(contraseña) > 14:
    print("La contraseña debe tener entre 8 y 14 caracteres.")
else:
    print("Contraseña válida.")

## Ejercicio 6
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean
print("Modo:", mode(numeros_aleatorios))
print("Mediana:", median(numeros_aleatorios))
print("Media:", mean(numeros_aleatorios))

## Ejercicio 7
