with open("07 Manejo de Archivos\productos.txt", "r") as archivo:
    for linea in archivo:
        producto, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}" )
        
        