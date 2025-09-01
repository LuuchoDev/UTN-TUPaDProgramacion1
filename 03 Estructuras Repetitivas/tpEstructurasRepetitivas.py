# =======================
#        EJERCICIO 1
# =======================

for i in range(101):
    print(i)

# =======================
#        EJERCICIO 2
# =======================

num = int(input("Ingrese un número: "))

## Convierto el numero a string y cuento la cantidad de digitos
cantDigitos = len(str(num))

## Imprimo la cantidad de dígitos                         
print("La cantidad de dígitos es:", cantDigitos)    

# =======================
#        EJERCICIO 3
# =======================

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

# =======================
#        EJERCICIO 4
# =======================

# Pide números al usuario y suma hasta que ingrese 0

num = int(input("Ingrese un número: "))
suma = 0

## Determino la suma de los números ingresados.
while num != 0:
    suma += num
    num = int(input("Ingrese un número: "))
print(f"La suma de los números ingresados es: {suma}")

# =======================
#        EJERCICIO 5
# =======================

import random
num = int(input("Adivine el número entre 0 y 9: "))
numRandom = random.randint(0, 9)
intentos = 1

## Bucle para adivinar el numero
while num != numRandom:
    intentos += 1
    num = int(input("Adivine el número entre 0 y 9: "))
print(f"¡Felicidades! Adivinaste el número {numRandom} en {intentos} intentos.")
# =======================
#        EJERCICIO 6
# =======================

for i in range (100, -1, -2):
    print(i)


# =======================
#        EJERCICIO 7
# =======================

num = int(input("Ingrese un número entero positivo: "))
suma = 0

# Suma todos los números desde 0 hasta el número ingresado.
for i in range(0, num + 1):
    suma += i
print(f"La suma de los números enteros positivos hasta {num} es: {suma}")

# =======================
#        EJERCICIO 8
# =======================

## Declaración de variables
par = 0
impar = 0
negativos = 0 
positivos = 0

# Pide 100 números al usuario y clasifica cada uno
for i in range (100):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num < 0:
        negativos += 1
    else:
        positivos += 1
    
print(f"Cantidad de números pares: {par}")
print(f"Cantidad de números impares: {impar}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")

# =======================
#        EJERCICIO 9
# =======================

suma = 0
for i in range (5):
    num = int(input("Ingrese un número: "))
    suma = suma + num
media = int(suma / 5)
print(f"La media de los números ingresados es: {media}")

# =======================
#        EJERCICIO 10
# =======================

num = int(input("Ingrese un número: "))
numInvertido = 0

# Invierte los dígitos del número
while num > 0:
    # Obtiene el último dígito
    digito = num % 10
    # Agrega el dígito al número invertido
    numInvertido = numInvertido * 10 + digito
    # Elimina el último dígito del número original
    num = num // 10
print(f"El número invertido es: {numInvertido}")