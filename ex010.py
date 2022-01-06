print("<===================> Currency converter <===================>")

Wallet = float(input("How much money do you have?: R$"))
ConvertedMoneyInDollar = Wallet / 5.57
ConvertedMoneyInEuro = Wallet / 6.33
ConvertedMoneyInPound = Wallet / 7.54
ConvertedMoneyInYen = Wallet / 0.05

print("You can buy {:.2F} dollars".format(ConvertedMoneyInDollar))
print("You can buy {:.2F} euros".format(ConvertedMoneyInEuro))
print("You can buy {:.2F} pounds".format(ConvertedMoneyInPound))
print("You can buy {:.2F} yens".format(ConvertedMoneyInYen))





print("<===================> Currency converter 2 <===================>")

Wallet = float(input("How much money do you have?: R$"))
print("You can buy {:.2f} dollars, {:.2f} euros, {:.2f} pounds and {:.2f} yen".format(Wallet / 5.57, Wallet / 6.33, Wallet / 7.54, Wallet / 0.05))


