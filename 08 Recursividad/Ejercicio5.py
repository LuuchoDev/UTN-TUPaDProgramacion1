def es_palindromo(palabra):
    palabra = palabra.lower().strip()
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_usuario = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra_usuario):
    print(f"La palabra '{palabra_usuario}' es un palíndromo.")
else:
    print(f"La palabra '{palabra_usuario}' no es un palíndromo.")