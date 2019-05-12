# Exercise 29 - Else and If

people = 30
cars = 40
trucks = 15

# Compares cars to people and if > it will print the first statement
# if not it will print the second statement
# if neither it will print the third statment
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# Compares trucks to cars and if > it will print the first statement
# if not it will print the second statement
# if neither it will print the third statment
if trucks > cars:
    print("That's too many trucks.")   
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

# Compares people to trucks and if > it will print the first statement
# if not it will print the second statement
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")