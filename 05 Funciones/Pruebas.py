def celsius_a_fahrenheit(celsius):
    ## Convierte grados Celsius a Fahrenheit.
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Ingrese la temperatura en Celsius: "))
print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(celsius)}")