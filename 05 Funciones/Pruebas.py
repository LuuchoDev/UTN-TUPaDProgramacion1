def segundos_a_horas(segundos):
    ## Esta función convierte segundos a horas.
    horas = segundos // 3600
    return horas
segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")