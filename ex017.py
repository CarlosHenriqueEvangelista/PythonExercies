import math

print("{:=^50}".format("> Discovering the hypotenuse <"))

OpossiteSide = int(input("Enter the opposite side: "))
AdjacentSide = int(input("Enter the adjacent side: "))

print("The hypotenuse is: {}".format(math.trunc(math.hypot(OpossiteSide, AdjacentSide))))



print("{:=^50}".format("> Discovering the hypotenuse <"))

OpossiteSide = float(input("Enter the opposite side: "))
AdjacentSide = float(input("Enter the adjacent side: "))

print("The hypotenuse is: {:.2f}".format((math.hypot(OpossiteSide, AdjacentSide))))



print("{:=^50}".format("> Discovering the hypotenuse <"))

OpossiteSide = float(input("Enter the opposite side: "))
AdjacentSide = float(input("Enter the adjacent side: "))
Hipotenuse = (OpossiteSide ** 2 + AdjacentSide ** 2 ) ** 0.5

print("The hypotenuse is: {:.2f}".format(Hipotenuse))
