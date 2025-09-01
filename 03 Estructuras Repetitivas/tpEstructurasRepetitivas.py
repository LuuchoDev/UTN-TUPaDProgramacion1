## Ejercicio 1

for i in range(101):
    print(i)
    
## Ejercicio 2

num = int(input("Ingrese un número: "))

## Convierto el numero a string y cuento la cantidad de digitos
cantDigitos = len(str(num))

## Imprimo la cantidad de dígitos                         
print("La cantidad de dígitos es:", cantDigitos)    

## Ejercicio 3

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

## Determino el menor y el mayor
menor = min(num1, num2)
mayor = max(num1, num2)

## Calculo la suma de los números entre el menor y el mayor
suma = 0
for i in range (menor + 1 , mayor):
    suma += i
print(f"La suma de los números entre {menor} y {mayor} es: {suma}")

## Ejercicio 4

# Pide números al usuario y suma hasta que ingrese 0

num = int(input("Ingrese un número: "))
suma = 0

## Determino la suma de los números ingresados.
while num != 0:
    suma += num
    num = int(input("Ingrese un número: "))
print(f"La suma de los números ingresados es: {suma}")

## Ejercicio 5

import random
num = int(input("Adivine el número entre 0 y 9: "))
numRandom = random.randint(0, 9)
intentos = 1

## Bucle para adivinar el numero
while num != numRandom:
    intentos += 1
    num = int(input("Adivine el número entre 0 y 9: "))
print(f"¡Felicidades! Adivinaste el número {numRandom} en {intentos} intentos.")

## Ejercicio 6

for i in range (100, -1, -2):
    print(i)


## Ejercicio 7

num = int(input("Ingrese un número entero positivo: "))
suma = 0

# Suma todos los números desde 0 hasta el número ingresado.
for i in range(0, num + 1):
    suma += i
print(f"La suma de los números enteros positivos hasta {num} es: {suma}")

## Ejercicio 8

