
# suma
answer = 30 + 12
print(answer)

# resta
difference = 30 - 12
print(difference)

# multiplicacion

product = 30 * 12
print(product)

# division
quotient = 30 / 12
print(quotient)

seconds = 1042
display_minutes = 1042 // 60

# modulo
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# ejercicio1
linea_vacia = "\n"
print(linea_vacia)

first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

# conversin de cadenas a numeros

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# valores absolutos

print(39 - 16)
print(16 - 39)

print(abs(39 - 16))
print(abs(16 - 39))

# redondeo

print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))

# biblioteca math

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# ejercicio 2

first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print(abs(distance_km))