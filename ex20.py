# Exercise 20 - Functions and Files

# imports argv from sys module
from sys import argv
# parameters required when using argv a script runtime
script, input_file = argv

# func print_all f = file.read
def print_all(f):
   # print(">>>> print_all f = ", f)
    print(f.read())
   # print("<<<< print_all f =", f)
# rewind to go to different spots in a line. 0 seems to be the first character
# in the line
def rewind(f):
    #print(">>>> rewind f = ", f)
    f.seek(0)
    #print("<<<< rewind f = ", f)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# This gets passed in as f in each function as a reference
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

# increments current line by 1
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
