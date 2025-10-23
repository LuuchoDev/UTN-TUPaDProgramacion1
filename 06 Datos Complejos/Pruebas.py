dia = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

agenda = {
    ("lunes", "10:00"): "Reunión equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "09:30"): "Entrega informe"
}

def consultar_agenda(dia,hora):
    clave = (dia, hora)
    if clave in agenda:
        return f"Actividad programada: {agenda[clave]}"
    else:
        return "No hay actividad programada en ese día y hora."

print (f"Días disponibles: {dia}")
dia = input("Ingrese un día de la semana: ").strip()
hora = input("Ingrese una hora (ej: 10:00): ").strip()

evento = consultar_agenda(dia, hora)
if evento: 
    print(f"En {dia} a las {hora}: {evento}")
else:
    print("No hay actividad programada en ese día y hora.")
