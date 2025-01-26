import pytz
import datetime
import calendar

# Función para mostrar la hora en una ciudad específica
def mostrar_hora_ciudad(ciudad):
    try:
        # Obtener la zona horaria de la ciudad
        zona_horaria = pytz.timezone(ciudad)
        hora_ciudad = datetime.datetime.now(zona_horaria).strftime("%H:%M:%S")
        print(f"La hora actual en {ciudad} es: {hora_ciudad}")
    except pytz.UnknownTimeZoneError:
        print(f"No se pudo encontrar la zona horaria para {ciudad}. Verifica el nombre de la ciudad.")

# Función para mostrar el calendario actual en una ciudad
def mostrar_calendario_ciudad(ciudad):
    try:
        # importar el año y mes actual segun la zona
        zona_horaria = pytz.timezone(ciudad)
        ahora = datetime.datetime.now(zona_horaria)
        año_actual = ahora.year
        mes_actual = ahora.month
        print(f"Calendario para {calendar.month_name[mes_actual]} {año_actual} en {ciudad}:")
        print(calendar.month(año_actual, mes_actual))
    except pytz.UnknownTimeZoneError:
        print(f"No se pudo obtener el calendario para {ciudad}. Verifica el nombre de la ciudad.")

# Ejemplo de como se usa
ciudad = input("Ingresa el nombre de la ciudad (ej. 'America/New_York', 'Europe/Madrid'): ")

mostrar_hora_ciudad(ciudad)
mostrar_calendario_ciudad(ciudad)
