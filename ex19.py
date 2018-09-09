# Exercise 19 - Functions and Variables

# This function will take input for the formated printing once the arguments are passed in below it
def chz_and_crackers(cheese_count, boxes_of_crackers):
    # print(">>> cheese_count = ", cheese_count, "boxes_of_crackers = ", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket and some wine.\n")
    # print("<<<<< exit cheese_and_crackers")


# Calls the function and runs it with 20, 30
print("1: We can just give the function numbers directly: ")
chz_and_crackers(20 , 30)

print("2: OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

# Calls the function and runs it with the arguments amount_of_cheese & amount_of_crackers
chz_and_crackers(amount_of_cheese, amount_of_crackers)

# Calls the function and does math inside the paramaters (cheese_count = 10 + 20) 
# (box_of_crackers = 5 + 6) 
print("3: We can even do math inside too: ")
chz_and_crackers(10 + 20, 5 + 6)

# Calls the function and passes the arguments amount_cheese 10 + 100, 
# and amount_of_crackers +1000
print("4: And we can combine the two, variables and math: ")
chz_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)