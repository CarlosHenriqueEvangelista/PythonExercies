print("{:=^50}".format("> Tax calculation <"))

ProductPrice = float(input("What is price of the product?: "))

print("You gotta pay 15% of tax, so the price will be: {:.2f}".format(ProductPrice + (ProductPrice * (15/100))))