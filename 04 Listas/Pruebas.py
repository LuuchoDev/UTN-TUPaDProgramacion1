# Inicializa el tablero 3x3 con guiones
tablero = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

## Muestra el tablero inicial
for fila in tablero:
    for celda in fila:
        print(celda, end=" ")
    print()
    
## Variables para controlar el juego
jugador = "x"
jugadas = 0

while jugadas < 9:
    print(f"\nTurno del jugador '{jugador}'")
    fila = int(input(f"Jugador '{jugador}', ingrese la fila (0-2): "))
    columna = int(input(f"Jugador '{jugador}', ingrese la columna (0-2): "))
    
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Coordenadas inválidas. Intente de nuevo.")
        continue # Salta a la siguiente iteración del bucle
    
    if tablero[fila][columna] != "-":
        print("La celda ya está ocupada. Intente de nuevo.")
        continue # Salta a la siguiente iteración del bucle

    # Realiza la jugada
    tablero[fila][columna] = jugador
    jugadas += 1

    # Verifica si hay un ganador
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
            print(f"¡El jugador '{jugador}' ha ganado!")
            jugadas = 9 # Termina el juego
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "-":
            print(f"¡El jugador '{jugador}' ha ganado!")
            jugadas = 9 # Termina el juego
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
        print(f"¡El jugador '{jugador}' ha ganado!")
        jugadas = 9 # Termina el juego
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
        print(f"¡El jugador '{jugador}' ha ganado!")
        jugadas = 9 # Termina el juego

    # Cambia de jugador
    jugador = "o" if jugador == "x" else "x"

    # Muestra el tablero
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()