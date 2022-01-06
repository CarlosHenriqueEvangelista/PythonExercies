print("{:_^20}".format("School average"))

FirstGrade = float(input("First Grade: "))
SecondGrade = float(input("Second Grade: "))
Media = (FirstGrade + SecondGrade) / 2

print("Media: {:.1f}".format(Media))



print("{:_^20}".format("School average 2"))

FirstGrade = float(input("First Grade: "))
SecondGrade = float(input("Second Grade: "))

print("Media: {:.1f}".format((FirstGrade + SecondGrade) / 2))

if(Media >= 6.0): {
  print("Student approved")
} 
else: {
  print("Student failed")
}