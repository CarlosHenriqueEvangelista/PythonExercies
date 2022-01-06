print("{:+^50}".format("Discounts and Increases"))

ProductPrice = float(input("What is the price of the product?: "))

Value = str(input("How do you want to pay, in cash or in installments?: "))

if(Value == "in cash"): {
  print("Paying in cash you get a 16% discount, so the price of the product is: {:.2f}".format(ProductPrice - (ProductPrice * (16/100))))
} 
if(Value == "installments"): {
  print("Paying installment you will have 8% increase, so the price of the product is: {:.2f}".format(ProductPrice + (ProductPrice * (8/100))))
} 