pennies = int(input("Enter an amount of pennies: "))

nickels = pennies//5
pennies = pennies - nickels * 5
print(nickels,"nickels and",pennies,"pennies")
