# Exercise 29 - What if

people = 20 
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print(">>> Count people:", people, "Count dogs:", dogs)
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs!")

## Study Drill ##
# 1. What do you think the if does to the code under it?
# It will evalute the statement and if it is true it will print.

# 2. Why does the code under the if need to be indented four spaces?
# Because python doesn't use {} so the indent acts as a code block.

# 3. What happens if it isn’t indented?
# You will get an indentation error.

# 4. Can you put other boolean expressions from Exercise 27 in the if-statement ? Try it.
#

# 5. What happens if you change the initial values for people , cats , and dogs ?
# The staements may no longer be true and not print anything