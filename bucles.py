
linea_vacia = " "
print(linea_vacia)

# Bucles while

# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')

    print(linea_vacia)

# ejercicios1
new_planet = ''
planets = []
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done')

print(planets)

# Bucles for
print(linea_vacia)

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

print(linea_vacia)

from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")
