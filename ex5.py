# Exercise 5 - More Variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue' 
teeth = 'White'
hair = 'Brown'
centemeters = 2.54
kilograms = 0.453592
height_to_centimeters = height * centemeters
weight_to_kilograms = weight * kilograms

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usuall {teeth} depening on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age} + {height} + {weight} I get {total}.")

# Experiment 1 height inches to height centemeters

print(f"If I want to convert {height} inches to centemeters: {height} * {centemeters} = {height_to_centimeters} centermeters.")

# Experiment 2 weight lbs to weight kilograms
print(f"If I want to convert {weight} lbs to kilograms: {weight} * {kilograms} = {weight_to_kilograms} kilograms.")