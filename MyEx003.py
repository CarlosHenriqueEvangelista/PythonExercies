print("{::^50}".format("> Temperature converted <"))

TemperatureInF = float(input("Enter the temperature in degrees °F: "))

print("This temperature converted to Celsius is: {:.2f}".format((TemperatureInF - 32) / 1.8))