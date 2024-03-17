fact = "the moon has not atmosphere."
two_facts = fact + "No sound can be heard on the moon."
print(two_facts)

linea_vacia = "\n"

moon_radius = "The moon has a radius  of 1,00miles."
moon2 = 'The "near side" is the part of the Moon thet faces the Earth.'
moon3 = "We only see about 60% of the Moon's surface."
moon4 = """We only see about 60% of the Moons surface, this is known as the "near side"."""

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline2 = """Facts aboout the Moon:
 There is no atmosphere.
 There is no sound."""
print(multiline2)

print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# Division de una cadena
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

# Busqueda de una cadena
print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())

print("The Moon And The Earth".upper())

# Comparacion del contenido de una cadena
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print("-60".startswith('-'))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# Transformar texto

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))


# Ejercicio 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.:"""

sentences = text.split('.')
print(sentences)

for sentences in sentences:
    if 'temperature' in sentences:
        print(sentences)

print(linea_vacia)
# Formateo de cadenas

# Formato de signo de porcentaje (%)

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth.\n" % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.\n""" % ("Moon", "Earth", "Moon", "Earth"))

# El metodo format

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.\n".format(mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.\n""".format("Moon", mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth\n.""".format(moon="Moon", mass=mass_percentage))

# acerca de las cadenas f-strings

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.\n")

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.\n")

subject = "interesting facts about the moon\n"
heading = f"{subject.title()}"
print(heading)

print(linea_vacia)

name = 'Ganymele'
planet = 'Mars'
gravity = '1.43'

template = """Gravity Facts about {name}
----------------------------------------
Planet name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))