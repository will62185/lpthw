# Exercise 38 - Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # Split the list on each word, adds a comma
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

# Some things in Python need to be written like len(stuff) and other times its stuff.pop()
while len(stuff) != 10: # Loop continues until it hits 10
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
