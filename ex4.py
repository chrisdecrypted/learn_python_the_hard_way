# Learn Python the Hard Way
# Accessed from https://learnpythonthehardway.org/python3/
# Exercise 4: Variables and Names
# Christopher Murray
# 7/4/2019

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars,"cars available.")
print("There are only", drivers, "drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

"""
comments go this way?
"""
#but python docs advise not to do this.