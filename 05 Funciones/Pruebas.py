def informacion_personal(nombre, apellido, edad, residencia):
    ## Esta función imprime la información personal del usuario.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)