# Exercise 14 - Prompting and Passing

from sys import argv

script, user_name, user_id = argv
prompt = '>> '
# Experimental prompt
prompt2 = "Location plz: "
# I kid around
prompt3 = "And why is it a sweet Ubuntu 18.04 PC? "

print(f"Hi {user_name}, userid: {user_id}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")

# You don't need have a variable here it will still work
# prompt from above is being passed into input
likes = input(prompt)

print(f"Where do you live {user_name}?")
# Experimental prompt
lives = input(prompt2)

print("What kind of computer do you have?")
computer = input(prompt3)

# Making the input prompt assigned to a var allowed me to f print
# them from the previous responses.
print(f"""
Alrighty {user_name}, so  I know your userid is {user_id}. 
You said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have {computer} computer. Nice!
""")