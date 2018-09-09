# Exercise 17 - More Files

from sys import argv
from os.path import exists

script, from_file, to_file, name = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
# print(">>>>> in_file =", repr(in_file))
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

# Exists checks if a path exists False if not True if yes
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input(f"What will it be {name}? ")

# opens the out_file which is the to_file was specified in argv and makes it writeable
out_file = open(to_file, 'w')
# writes the contents of indata to out_file
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
# print(">>>>>in_file = ", repr(in_file.close))