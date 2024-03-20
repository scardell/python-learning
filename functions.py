# Aspectos basicos de las funciones
# Funciones sin argumentos

def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()

output = rocket_parts()

output is None

def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

# Argumentos opcionales y requeridos

linea_vacia = " "
print(linea_vacia)

any([True, False, False]) # output: True
any([False, False, False]) # output: False
str()   # output: ''
str(15) # output: '15'

# uso de argumentos de funcion

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

distance_from_earth("Moon")

distance_from_earth("Saturn")

# varios argumentos necesarios

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(238855, 75)  # output: 132.697222

# Funciones como argumentos

total_days = days_to_complete(238855, 75)
round(total_days) # output: 133

round(days_to_complete(238855, 75)) # output: 133

# ejercicio1

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)

# uso de argumentos de palabras clave

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

# Combinacion de argumentos y argumentos de palabras clave

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon"))
print(arrival_time("Mars", 100))

# print(linea_vacia)

# Uso de argumentos de variable

def variable_length(*args):
    print(args)

variable_length()

variable_length("one", "two")

variable_length(None)

print(linea_vacia)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(5, 10, 15))

# argumentos de palabra clave variable
print(linea_vacia)

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)

print(linea_vacia)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

print(linea_vacia)

# Ejercicio 2

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)


