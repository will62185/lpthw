# Exercise 11 - Asking Questions

# We put a end=' ' at the end of each print line. This tells print to not end
# the line with a newline character and go to the next line.

print("What is your name?", end = ' ')
name = input()
print("How old are you?", end=' ')
age = int(input())
# print(">>>> Debugging >>>> age = ", repr(age))
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"{name}, you're {age} years old, {height} tall, and you weigh {weight}")