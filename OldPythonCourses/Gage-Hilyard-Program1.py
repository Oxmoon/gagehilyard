# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Gage Hilyard
# Last Modified: January 25, 2019 
# ---------------------------------------
# Calculates GPA from user input
# ---------------------------------------
import math

def translate(letter, credit):
    letter_grade = 0.0
    if letter == 'a' or letter == 'A':
        letter_grade = 4.0

    if letter == 'a-' or letter == 'A-':
        letter_grade = 3.7

    if letter == 'b+' or letter == 'B+':
        letter_grade = 3.3

    if letter == 'b' or letter == 'B':
        letter_grade = 3.0

    if letter == 'b-' or letter == 'B-':
        letter_grade = 2.7

    if letter == 'c+' or letter == 'C+':
        letter_grade = 2.3

    if letter == 'c' or letter == 'C':
        letter_grade = 2.0

    if letter == 'c-' or letter == 'C-':
        letter_grade = 1.7

    if letter == 'd+' or letter == 'D+':
        letter_grade = 1.3

    if letter == 'd' or letter == 'D':
        letter_grade = 1.0

    if letter == 'f' or letter == 'F':
        letter_grade = 0.0

    return letter_grade*credit
        
# +------------------------------------------------------------------------------------------

def main():
    grade = 0
    total_credits = 0
    number_of_courses = int(input('Enter the number of courses you are taking: '))
    print('')
    for course_number in range(number_of_courses):
        letter = input('Enter grade for course '\
                       +str(course_number+1) +': ')
        credit = int(input('Enter credits for course ' +str(course_number+1) +': '))
        print('')
        grade = grade + translate(letter, credit)
        total_credits = total_credits + credit
    final_grade = float(grade/total_credits)
    final_grade = str(round(final_grade, 2))
    print('Your GPA is ' +str(final_grade))

# +-----------------------------------------------------------------------------------------

main()
