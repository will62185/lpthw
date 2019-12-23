# Exercise 33 While Loops

index = 0
numbers = []

while index < 6:
    print(f"At the top index is {index}")
    numbers.append(index)

    index = index + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom index is {index}")

print("The numbers: ")

for number in numbers:
    print(number)