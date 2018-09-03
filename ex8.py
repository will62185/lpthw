# Exercise 8 - Printing, Printing

# Assigns curly braces to formatter variable
# Seems we are doing this to be able to use .format later on
formatter = "{} {} {} {}"

# In place of {} in formatter we will use 1, 2, 3, 4
print(formatter.format(1, 2, 3, 4))

# In place of {} in formatter we will use one, two, three, four
print(formatter.format("one", "two", "three", "four") )

# In place of {} in formatter we use True, False, False, True
# It seems that bool values are special and don't need " "
print(formatter.format(True, False, False, True))

# This was interesting, it prints what is insdie formatter {}(4) x 4 = 16
print(formatter.format(formatter, formatter, formatter, formatter))

# Prints the text which is separated by a line brack on the same line
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))