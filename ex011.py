print("{:=^50}".format(" Painting the wall "))

Width = float(input("How wide is the wall?: "))
Height = float(input("How high is the wall?: "))
Area = Width * Height
LitersOfPaint = Area / 2

print("It will be necessary {} liters to paint the wall taking into account that the area is {}".format(LitersOfPaint, Area))

print("{:=^50}".format(" Painting the wall 2"))

Width = float(input("How wide is the wall?: "))
Height = float(input("How high is the wall?: "))

print("It will be necessary {} liters to paint the wall taking into account that the area is {}".format((Width * Height) / 2, Width * Height ))
