# Exercise 39  - Dictionaries, Oh Lovely Dictionaries

things = ["a", "b", "c", "d"]
print(things[1])

things[1] = "z"
print(things[1])

print(things)

stuff = {
    "name": "Zed",
    "age": 39,
    "height": 6 * 12 + 2 
}
# Add stuff to dicts
print(stuff["name"])
print(stuff["age"])
print(stuff["height"])
stuff["city"] = "SF"
print(stuff["city"])
print(stuff)
stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
print(stuff)

# Delete stuff from dict using pop
stuff.pop("city")
stuff.pop(1)
stuff.pop(2)
print(stuff)

'''
A Dictionary Example:
We’ll now do an exercise that you must study very carefully. 
I want you to type this code in and try to understand what’s going on. 
Take note of when you put things in a dict, get them from a hash, and all the operations you use. 
Notice how this example is mapping states to their abbreviations and then the abbreviations to cities in the states. 
Remember, ”mapping” or ”associating” is the key concept in a dictionary.
'''
# create a mapping of state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print("-" * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()): # Key, Value = "state":"abbrev"
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    print("-" * 10)

# safely get an abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX'  is: {city}")

