print("{:.^50}".format("> Discounted price <"))

PriceOfTheProduct = float(input("What is the price of the product?: R$"))
Discounted = 5/100
DiscountedPrice = PriceOfTheProduct * Discounted
FinalPrice = PriceOfTheProduct - DiscountedPrice


print("On sale, the product will have a 5% discount, leaving: R${:.2f}".format(FinalPrice))

print("{:.^50}".format("> Discounted amount 2 <"))

PriceOfTheProduct = float(input("What is the price of the product?: R$"))


print("On sale, the product will have a 5% discount, leaving: R${:.2f}".format(PriceOfTheProduct - (PriceOfTheProduct * (5/100) )))

