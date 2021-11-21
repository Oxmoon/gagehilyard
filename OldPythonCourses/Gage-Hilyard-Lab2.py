# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Lab 2: Tax Calculator                 |
# Gage Hilyard                          |
# Date: January 24, 2019                |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2018.  |
# ---------------------------------------

def unmarried_individual_tax(income):
    tax_owed = 0

    if income > 0 and income < 9700:
        tax_owed = income * 0.10
        
    elif income > 9700:
        tax_owed = 9700 * 0.10
        
    if income > 9700 and income < 39475:
        tax_owed = tax_owed + (income-9700) * 0.12
        
    elif income > 39475:
        tax_owed = tax_owed + ((39475-9700) * 0.12)

    if income > 39475 and income < 84200:
        tax_owed = tax_owed + (income-39475) * 0.22
        
    elif income > 84200:
        tax_owed = tax_owed + ((84200-39475) * 0.22)

    if income > 84200 and income < 160725:
        tax_owed = tax_owed + (income-84200) * 0.24
        
    elif income > 160725:
        tax_owed = tax_owed + ((160725-84200) * 0.24)

    if income > 160725 and income < 204100:
        tax_owed = tax_owed + (income-160725) * 0.32
        
    elif income > 204100:
        tax_owed = tax_owed + ((204100-160725) * 0.32)

    if income > 204100 and income < 510300:
        tax_owed = tax_owed + (income-204100) * 0.35
        
    elif income > 510300:
        tax_owed = tax_owed + ((510300-204100) * 0.35) + ((income-510300) * 0.37)

    return tax_owed  

# ---------------------------------------

def process(income):
    print("The 2018 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()
