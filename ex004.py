Something = input("Enter something: ")
type = type(Something)
Alphanumeric = Something.isalnum()
Alpha = Something.isalpha()
Ascii = Something.isascii()
Decimal = Something.isdecimal()
Digit = Something.isdigit()
Indentifier = Something.isidentifier()
Lower = Something.islower()
Upper = Something.isupper()
Numeric = Something.isnumeric()
Printable = Something.isprintable()
Space = Something.isspace()
Title = Something.istitle()

print("type:", type)
print("Alphanumeric: ", Alphanumeric)
print("Alpha:", Alpha)
print("Ascii:", Ascii)
print("Decimal:", Decimal)
print("Digit:", Digit)
print("Indentifier:", Indentifier)
print("Lower:", Lower)
print("Upper:", Upper)
print("Numeric:", Numeric)
print("Printable:", Printable)
print("Space:", Space)
print("Title:", Title)

#Type() says the type of the value

#Aphanumeric returns true with numbers, letters and both together

#Alpha and indentifier returns true with latters
#Ascii and Printable returns true with everything

#Decimal, Digit and Numeric returns true with numbers

#Lower returns true with a word written entirely in lowercase

#Upper returns true with a word written entirely in uppercase

#Title returns true with a word with the first letter in uppercase and the rest in lower case

#Space returns true with only space