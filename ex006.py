print("{:=^50}".format(": Double, Triple and Square root :"))

SomeNumber = int(input("Enter a number: "))
Double = SomeNumber * 2
Triple = SomeNumber * 3
SquareRoot = SomeNumber ** (1/2)

print("Double: {}".format(Double))
print("Triple: {}".format(Triple))
print("SquareRoot: {:.2f}".format(SquareRoot))

print("{:=^50}".format(": Double, triple and Square root 2 :"))

SomeNumber = int(input("Enter a number: "))

print("Double: {} \nTriple: {} \nSquareRoot: {:.2f}".format(SomeNumber * 2, SomeNumber * 3, SomeNumber ** (1/2)))