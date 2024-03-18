
# listas en Python

# Acceso a elementos de lista or indice

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
print("The fourth planet is", planets[3])

planets[3] = "Red Planet" # cambio de valor mediante indice
print("Mars is also known as", planets[3])

linea_vacia = '\n'
print(linea_vacia)

# Longitud de una lista
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Incorporar elementos a una lista con .append(value)

planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

print(linea_vacia)

# Eliminar elementos de una lista con .pop(index) o el ultimo elemento con .pop()

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

print(linea_vacia)

# uso de indices negativos para acceder a elementos de una lista

print("The first planet is", planets[0])

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

print(linea_vacia)

# busqueda de un valor en una lista

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")

print(linea_vacia)
# ejercicio1

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)

print("There are", len(planets), "planets")

planets.append("Pluto")
print("Actualy, there are", len(planets), "planets")
print(planets[-1], "is the last planet")

print(linea_vacia)

# trabajo con numeros en una lista

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")

# Uso de min() y max() en una lista

print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

print(linea_vacia)

# Manipulacion de datos en una lista
# Segmentation de listas

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth) 

planets_after_earth = planets[3:]
print(planets_after_earth)

# Combinacion de listas

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# ordenacion de listas

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

print(linea_vacia)

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

print(linea_vacia)
# ejercicio2

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

user_planet = input("Please enter the name of the planet (with a capital letter to start)")

planet_index = planets.index(user_planet)

print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])
