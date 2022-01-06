import math

print("{:=^50}".format("> Discovering the hypotenuse <"))

OpossiteSide = int(input("Enter the opposite side: "))
AdjacentSide = int(input("Enter the adjacent side: "))

print("The hypotenuse is: {}".format(math.trunc(math.hypot(OpossiteSide, AdjacentSide))))