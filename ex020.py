import random

print("{:=^50}".format("> Choosing an order <"))

NameOne = str(input("Enter a name: "))
NameTwo = str(input("Enter a name: "))
NameThree = str(input("Enter a name: "))
NameFour = str(input("Enter a name: "))

RandomOrder = [NameOne, NameTwo, NameThree, NameFour]

random.shuffle(RandomOrder)
 
print("The order chosen was: {}".format(RandomOrder))