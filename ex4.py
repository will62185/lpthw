# Exercise 4 - Variables and Names

# 100 = cars
cars = 100
# 4.0 = space_in_a_car
space_in_a_car = 4.0
# 30 = drivers
drivers = 30
# 90 = passengers
passengers = 90
# cars_not_driven = 100 - 30
cars_not_driven = cars - drivers
# 30 = cars_driven
cars_driven = drivers
#carpool_capacity = 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = 90 / 30
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today,")
print("We need to put about", average_passengers_per_car, "in each car.")