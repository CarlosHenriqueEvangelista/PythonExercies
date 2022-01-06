import math

print("{:=^50}".format("> Elimating Floating Numbers <"))

NumberWithFloatingNumber = float(input("Enter a floating number to convert it to an integer: "))

print("This number with only it's integer part is: {}".format(math.trunc(NumberWithFloatingNumber)))


