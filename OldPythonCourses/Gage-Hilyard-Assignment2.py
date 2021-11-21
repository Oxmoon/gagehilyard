# -----------------------------------------
# Gage Hilyard                                
# CSCI 107, Assignment 2                   
# Last Updated: September 14, 2018            
# -----------------------------------------
# Prints a name card with with the user's
# name and phone number on a business card
# -----------------------------------------

FirstName= input("First Name: ")
LastName= input("Last Name: ")
FullName= FirstName +", " +LastName
WorkNumber= input("Work Phone Number in format (XXX)XXX-XXXX: ")
email = str(FirstName.lower()+"@parasail.com")

print("")
print("Here is your business card ...")
print("")
print("+------------------------------------------------+")
print("|    |                                           |")
print("|   -|          " +FullName.ljust(33) +         "|")
print("|  --|          Tribute Liabilities Associate    |")
print("| ---|          Parasail Capital                 |")
print("| ---------                                      |")
print("|  -------      4 Hunger Plaza                   |")
print("|               STE 1400                         |")
print("|               District 12, Panem 00012         |")
print("|                                                |")
print("| Work: "+WorkNumber ,"  @: " +email.ljust(22) +"|")
print("+------------------------------------------------+")
