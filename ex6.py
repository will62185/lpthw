# Exercise 6 - Strings and Text

# assign 10 to types_of_people
types_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

# assign "binary" to binary
binary = "binary"
# assign "don't" to do_not
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# It seems you need to have an empty curly brace in order to add hilarious
# since its a bool value into a str value
joke_evaluation = "Isn't that joke so funny?! {}"

# Changing .format() can break this line 
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Adds var w and e together to print one line
# Needs to be of same type string to not error
# Although you can convert a number to a string by e.g. str(2)
print(w + e)