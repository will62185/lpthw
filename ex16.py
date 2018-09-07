# Exercise 16 - Reading and Writing Files

from sys import argv

script, filename, username = argv

print(f"We're going to erase {filename}")
print("If you want that, type CTRL-C (^C) now.")
print("If you do want that hit RETURN now.")
# Jazzed this up a bit
input(f"Need an answer meow {username}: ")

print("Opening the file... ")
# Opens a file that is passed by the user through argv
# If the file doesn't exist it will be created and then be writeable
# because of the argument 'w' passed
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
# deletes anything that is in the file
# not needed because w deletes the file from the beginning
#target.truncate()

print("Now I'm going to ask you for three lines or else.")
# Whatever was input from the user is stored in line1, line2, line3
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file now . . .")
# This will write to the file what was stored in line1, line2, line3
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it. . . ")
target.close()
# Study drill
print("But afterwards we can open it: \n")
txt = open(filename)
print(txt.read())

# You should have seen all sorts of commands (methods/functions) you can give to files. 
# Here’s the list of commands I want you to remember:
# • close – Closes the file. Like File->Save.. in your editor.
# • read – Reads the contents of the file. You can assign the result to a variable.
# • readline – Reads just one line of a text file.
# • truncate – Empties the file. Watch out if you care about the file.
# • write('stuff') – Writes ”stuff” to the file.
# • seek(0) – Move the read/write location to the beginning of the file.

#The argument mode points to a string beginning with one of the following
# sequences (Additional characters may follow these sequences.):

# ``r''   Open text file for reading.  The stream is positioned at the
#         beginning of the file.

# ``r+''  Open for reading and writing.  The stream is positioned at the
#         beginning of the file.

# ``w''   Truncate file to zero length or create text file for writing.
#         The stream is positioned at the beginning of the file.

# ``w+''  Open for reading and writing.  The file is created if it does not
#         exist, otherwise it is truncated.  The stream is positioned at
#         the beginning of the file.

# ``a''   Open for writing.  The file is created if it does not exist.  The
#         stream is positioned at the end of the file.  Subsequent writes
#         to the file will always end up at the then current end of file,
#         irrespective of any intervening fseek(3) or similar.

# ``a+''  Open for reading and writing.  The file is created if it does not
#         exist.  The stream is positioned at the end of the file.  Subse-
#        quent writes to the file will always end up at the then current
#         end of file, irrespective of any intervening fseek(3) or similar.
