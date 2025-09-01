import random
num = int(input("Adivine el número entre 0 y 9: "))
numRandom = random.randint(0, 9)
intentos = 1

## Bucle para adivinar el numero
while num != numRandom:
    intentos += 1
    num = int(input("Adivine el número entre 0 y 9: "))
print(f"¡Felicidades! Adivinaste el número {numRandom} en {intentos} intentos.")