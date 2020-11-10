"""
Author: Manuel Brito
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B.

Este programa lo resuelvo de la siguiente forma:
Primero pido al usuario a qué hora salió del punto A; en horas, minutos y segundos.
Luego esta cantidad la paso a segundos, para poder sumarla con el tiempo de viaje.
Y finalmente muestro la hora de llegada del usuario hasta el punto B.

"""

def convert_h_to_s(hours):
    return hours * 3600

def convert_m_t_s(minutes):
    return minutes * 60

def sum_h_m_s(hours, minutes, seconds):
    return convert_h_to_s(hours) + convert_m_t_s(minutes) + seconds

def convert_s_to_h_m_s(seconds):
    hours = seconds // 3600
    rest_seconds = seconds % 3600
    minutes = rest_seconds // 60
    segundos = rest_seconds % 60

    return {
            'min' : minutes,
            'hour' : hours,
            'sec' : segundos
            }

# Programa principal
try:
    time_cyclist_h = int(input("A qué hora saliste?: "))
    time_cyclist_m = int(input("Minutos: "))
    time_cyclist_s = int(input("Segundos: "))

    travel_time = int(input("¿Cuántas horas tardaste?: "))
    travel_time *= 3600
    total_time = travel_time + sum_h_m_s(time_cyclist_h, time_cyclist_m, time_cyclist_s)
    final_time = convert_s_to_h_m_s(total_time)
    print(f"La hora de llegada es {final_time.get('hour')}:{final_time.get('min')}")
except:
    print("ERROR")


















