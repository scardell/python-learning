
linea_vacia = " "

# creación de un diccionario

planet = {
    'name': 'Earth',
    'moons': 1
}
# lecctura de valores de un diccionario

print(planet.get('name'))

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

wibble = planet.get('wibble') # Returns None

#wibble = planet['wibble'] # Throws KeyError

# Modificación de valores de un diccionario

planet.update({'name': 'Makemake'})

# No output: name is now set to Makemake.

planet['name'] = 'Makemake'

# No output: name is now set to Makemake.

planet.update({
    'name': 'Jupiter',
    'moons': 79
})
planet['name'] = 'Jupiter'
planet['moons'] = 79

#adición y eliminacion de claves

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# tipos de datos complejos

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

# Para recuperar valores en un diccionario anidado, debe encadenar corchetes o llamadas a get.
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

print(linea_vacia)

# ejercicio1

planet = {
    'name': 'Earth',
    'moons': 1
}

print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet['circumference (km)'] = {
    'polar': 40008,
    'equatorial': 39614
}

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

print(linea_vacia)

# programacion dinamica con diccionarios

# recuperacion de todas las claves de un diccionario

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
    
# determinacion de si una clave existe en un diccionario

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1

# recuperacion de todas los valores de un diccionario

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')

print(linea_vacia)

# ejercicio2

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')
