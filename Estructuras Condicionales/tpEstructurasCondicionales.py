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
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

## Ejercicio 8
nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese el numero 1, 2 o 3: "))
if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
    
## Ejercicio 9
magnitud = int(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

## Ejercicio 10

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el día: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Es invierno.")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Es primavera.")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Es verano.")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Es otoño.")
elif hemisferio == "S":
    if (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Es invierno.")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Es primavera.")
    elif (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Es verano.")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Es otoño.")
else:
    print("Ingrese un hemisferio válido.")