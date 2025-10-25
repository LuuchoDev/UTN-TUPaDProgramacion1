def leer_productos():
    productos = []
    with open("07 Manejo de Archivos\productos.txt", "r") as archivo:
        for linea in archivo:
            producto, precio, cantidad = linea.strip().split(",")
            productos.append({"nombre": producto, "precio": precio, "cantidad": cantidad})
    return productos

def buscar_producto(producto, nombre_productos):
    for producto in producto:
        if producto["nombre"].lower() == nombre_productos.lower():
            return producto
    return None

productos = leer_productos()
nombre_producto = input("Ingrese el nombre del producto a buscar: ")
producto_encontrado = buscar_producto(productos, nombre_producto)

if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado}")
else:
    print("El producto no existe.")