productos = {"manzana": 50, "banana": 30}

def consultar_stock():
    nombre = input("Ingrese el nombre del producto a consultar: ")
    if nombre in productos:
        print(f" Stock de '{nombre}': {productos[nombre]} unidades.")
    else:
        print(f" El producto '{nombre}' no se encuentra en el inventario.")

def agregar_actualizar_stock():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad a agregar para '{nombre}': "))

    if nombre in productos:
        # Si existe, suma al stock actual
        productos[nombre] += cantidad
        print(f" Stock de '{nombre}' actualizado. Nuevo total: {productos[nombre]} unidades.")
    else:
        # Si no existe, lo crea con el stock inicial
        productos[nombre] = cantidad
        print(f" Producto '{nombre}' agregado con un stock de {cantidad} unidades.")

# Bucle principal del programa
while True:
    print("\n--- Sistema de Inventario ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar/Actualizar stock de un producto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        consultar_stock()
    elif opcion == '2':
        agregar_actualizar_stock()
    elif opcion == '3':
        print("Saliendo del sistema. chaito!!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
