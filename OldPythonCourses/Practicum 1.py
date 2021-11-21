# Question 1
##
##birth_year = int(input("Enter your birth year: "))
##current_year = 2019
##print("Happy Birthday! You are " +str(current_year - birth_year) +" years old.")

#Question 2

##def cribbage_sequence(card_list):
##    card_list.sort()
##    first_card = card_list[0]
##    second_card = card_list[1]
##    third_card = card_list[2]
##    if (first_card == second_card - 1) and (second_card == third_card - 1):
##        return True
##    else:
##        return False
##
##
##print(cribbage_sequence([4,2,3]))
##print(cribbage_sequence([2,3,4]))
##print(cribbage_sequence([5,7,8]))

# Question Three
import random
import string
def generate_password(length):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    password = ""
    for i in range(length):
        password += alphabet[random.randint(0,51)]
    print(password)


generate_password(10)


