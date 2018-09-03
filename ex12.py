# Exercise 12 - Prompting People

name = input("What is your name? ")
age = input("How old are you? ")
height = input(f"You're {age} years old. Nice. How tall are you? ")
weight = input("How much do you weigh? ")

print(f"{name}, you're {age} years old, {height} tall, and you weigh {weight}.")


# Use pydoc3 to also read about open, file, os, and sys. It’s alright if you do not understand those;
# just read through and take notes about interesting things.
# sudo pydoc3 -p 80 Starts a webserver to see the doc
# add an alias to .bashrc to cover pydoc=pydoc3