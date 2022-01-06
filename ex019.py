import random 

print("{:=^50}".format("> Raffling names <"))

NameOne = str(input("Enter a name: "))
NameTwo = str(input("Enter a name: "))
NameThree = str(input("Enter a name: "))
NameFour = str(input("Enter a name: "))

print("The name chosen was: {}".format(random.choice([NameOne, NameTwo, NameThree, NameFour])))