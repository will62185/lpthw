# Exercise 15 - Reading Files

from sys import argv

script, filename = argv

# Explanation below
txt = open(filename)
# txt = open(filename, 'w')
# txt.close()
# txt.write('test')

# format prints filename from user input in argv
print(f"Here's your file {filename}: ")
# reads the text file to end of file
# .read is working from the var txt = open(filename)
# txt.read() is saying to read itself
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# Does txt = open(filename) return the contents of the file? No, it doesn’t. It actually makes something
# called a ”file object.” You can think of a file like an old tape drive that you saw on mainframe
# computers in the 1950s or even like a DVD player from today. You can move around inside
# them and then ”read” them, but the DVD player is not the DVD the same way the file object is
# not the file’s contents.