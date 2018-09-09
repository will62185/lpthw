# Exercise 19: Study drill

def pizza_pie(nyc_style, chicago_style):
    print(f"You prefer {nyc_style} NYC Style Pizza")
    print(f"You prefer {chicago_style} Chicago Style Pizza")
    input("Which toppings do you prefer?")
    print(f"I like {input})

nyc_style = "thin crust"
chicago_style = "deep dish" 

pizza_pie(nyc_style, chicago_style)
