print("{::^50}".format("> Salary increase <"))

Salary = float(input("What is your salary?: R$"))
Increase = 15/100
SalaryIncrease = Salary * Increase
SalaryFinal = Salary + SalaryIncrease

print("Congratulations, you received a 15% raise, now your salary is: R${:.2f}".format(SalaryFinal))


print("{::^50}".format("> Salary increase 2 <"))

Salary = float(input("What is your salary?: R$"))

print("Congratulations, you received a 15% raise, now your salary is: R${:.2f}".format(Salary + (Salary * (15/100))))
