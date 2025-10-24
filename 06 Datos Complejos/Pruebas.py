original = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Uruguay": "Montevideo"
}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print(invertido)