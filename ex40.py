# Exercise 40 - Modules, Classes, and Objects

### Modules are like dictionaries

'''
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

Once I have this code, I can use the module MyStuff with import and then access the apple function:

import mystuff

mystuff.apple()
I could also put a variable in it named tangerine:

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

I can access that the same way:

import mystuff

mystuff.apple()
print(mystuff.tangerine)

Refer back to the dictionary, and you should start to see how this is similar to using a dictionary, but the
syntax is different. Let’s compare:

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

This means we have a very common pattern in Python:
1. Take a key=value style container.
2. Get something out of it by the key’s name.
In the case of the dictionary, the key is a string and the syntax is [key]. In the case of the module, the
key is an identifier, and the syntax is .key. Other than that they are nearly the same thing
'''

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

### I now have three ways to get things from things:

'''
# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
'''

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy brithday to you",
                    "I dont want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                         "With pokets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

