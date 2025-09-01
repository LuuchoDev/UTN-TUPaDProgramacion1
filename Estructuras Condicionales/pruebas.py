a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a != b:
    division = a / b
    print("La división de", a, "entre", b, "es:", division)
elif b != 0:
    division = b / a
    print("La división de", b, "entre", a, "es:", division)
else:
    print("Los números son iguales, no se puede realizar la división.")
