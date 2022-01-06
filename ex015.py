print("{:-^50}".format("> Car rental <"))

NumberOfDaysTheCarWasUsed = int(input("How many days has the car been used?: "))
KmTheCarTraveled = float(input("How many km did car traveled?: "))

print("The amount you gotta to pay for the car is: US${}".format(NumberOfDaysTheCarWasUsed * 60 + KmTheCarTraveled * 0.15))