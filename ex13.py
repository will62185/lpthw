# Exercise 13 - Parameters, Unpacking, Variables

# argv = argument variable. These are modules also libraries.
# Modules give you features
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

# Debug what does argv do?
# Always be printing to know what the program is doing
print(">>>> argv = ", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
# print("")

# WYSS: To run you must pass arguments at run time
# python ex13.py first 2nd 3rd