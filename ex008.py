print("{:^^30}".format("Measurement^converter"))

Meters = int(input("Meters: "))

Kilometers = Meters * 0.001
Hectometer = Meters * 0.01
Dekameter = Meters * 0.1
Decimeter = Meters * 10
Centimeter = Meters * 100
Melimeters = Meters * 1000

print("Kilometers: {}".format(Kilometers))
print("Hectometer: {:.2f}".format(Hectometer))
print("Dekameter: {:.1f}".format(Dekameter))
print("Decimeter: {}".format(Decimeter))
print("Centimeters: {}".format(Centimeter))
print("Melimeters: {}".format(Melimeters))

print("{:^^30}".format("Measurement^converter"))

Meters = int(input("Meters: "))

print("Kilometers: {} \nHectometer: {} \nDekameter: {} \nDecimeter: {} \nCentimeters: {} \nMelimeters: {}".format(Meters * 0.001, Meters * 0.01, Meters * 0.1, Meters * 10, Meters * 100, Meters * 1000))