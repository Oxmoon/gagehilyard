# -----------------------------------------
# Gage Hilyard                                
# CSCI 107, Assignment 10                  
# Last Updated: December 7, 2018         
# -----------------------------------------
# Describe the assignment briefly here.    
# -----------------------------------------

import string

# -----------------------------------------+
# all_digits                               |
# -----------------------------------------+
# user_string: The string to test          |
# -----------------------------------------+
# Return True if user_string only contains |
# digits.  Return False otherwise.         |
# -----------------------------------------+

def all_digits(user_string):
    for ch in user_string:
        if ch not in string.digits:
            return False
    return True

# -----------------------------------------+
# get_dimension                            |
# -----------------------------------------+
# message: The message to print.           |
# low: The smallest integer allowed.       |
# high: The largest integer allowed.       |
# -----------------------------------------+
# Prompt the user to enter an integer      |
# between low and high.                    |
# -----------------------------------------+

def get_dimension(message, low, high):
    done = False
    dimension_range = " [" + str(low) + ":" + str(high) + "]: "
    while (not done):
        answer = input("Enter the number of " + message + dimension_range)
        if all_digits(answer):
            answer = int(answer)
            if (answer >= low) and (answer <= high):
                done = True
            else:
                print("Error: the number is out of range.  Please try again.")
        else:
            print("Error: a non-digit was entered.  Please try again.")
    return answer

# -----------------------------------------+
# multiplication_table                     |
# -----------------------------------------+
# numRow: Number of rows in multiplication |
# table.                                   |
# numCol: Number of columns in             |
# multiplication table.                    |
# -----------------------------------------+
# Prints a multiplication table of a given |
# size.                                    |
# -----------------------------------------+

def multiplication_table(numRow, numCol):
    # makes top row
    topRow= ""
    for i in range(1, numCol+1):
        number = str(i)
        topRow += number.rjust(5)+" "

    # divider row
    divider= "  "+("+"+"-"*5)*numCol+"+"

    # prints all in order
    print("  "+topRow)
    for y in range(1, numRow+1):
        print(divider)
        tableRow(y, numCol)
    print(divider)


# Helper function
# Uses rowNumber(y) and numCol given by
# the multiplication_table for loop.

def tableRow(rowNumber, numCol):
    string = str(rowNumber).rjust(2)+"|"
    for i in range(1, numCol+1):
        number = str(rowNumber*i)
        string += number.rjust(4)+" |"
    print(string)

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Prompt the user for the dimensions of    |
# multiplication table.  Then print it.    |
# -----------------------------------------+

def main():
    print("\nAssignment 10: Multiplication Table\n")
    rows = get_dimension("rows", 1, 25)
    columns = get_dimension("columns", 1, 25)
    multiplication_table(rows, columns)

# -----------------------------------------+

main()
