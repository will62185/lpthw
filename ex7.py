# Exercise 7 - More Printing

print("Mary had a little lamb.")
# format prints snow where the {} exists in the line
# A variable wouldn’t have the single-quotes around it.
print("Its fleece was white as {}.".format('snow'))

print("And everywhere that Mary went.")
# prints . x 10 times
print("." * 10) # what'd that do?

# Can I use single-quotes or double-quotes to make a string or do they do different things? In Python either
# way to make a string is acceptable, although typically you’ll use single-quotes for any short
# strings like 'a' or 'snow'.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# end =' ' looks to add a space bettween print1 and print2
# I can also add in a '\n' to add a space between the two
# Prints out Cheese Burger
print(end1 + end2 + end3 + end4 + end5 + end6, end =' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
