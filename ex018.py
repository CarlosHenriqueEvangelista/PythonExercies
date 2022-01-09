import math

print("{:=^50}".format("> Sine, Cosine and Tangent <"))

Angle = float(input("Enter a angle to see your Sine, Cosine and Tangent: "))

print("Sine: {:.2f}".format(math.sin(math.radians(Angle))))
print("Cosine: {:.2f}".format(math.cos(math.radians(Angle))))
print("Tangent: {:.2f}".format(math.tan(math.radians(Angle))))