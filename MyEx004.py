import math

print("{::^50}".format("> Rounding <"))

SomeFloatingNumber = float(input("Enter a number that will be rounded: "))

print("Rounded number up: {}".format(math.ceil(SomeFloatingNumber)))
print("Rounded number down: {}".format(math.floor(SomeFloatingNumber)))

