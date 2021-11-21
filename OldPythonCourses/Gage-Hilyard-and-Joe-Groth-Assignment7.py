# -----------------------------------------+
# Gage Hilyard and Joe Groth                             
# CSCI 107, Assignment 7                   
# Last Updated: November 1, 2018            
# -----------------------------------------
# Manufactoria   
# -----------------------------------------

# -----------------------------------------------------------+
# function four_or_more_reds: Tests string for four or more
# reds in the string.
# -----------------------------------------------------------+
# string: the string used in the test
# -----------------------------------------------------------+

def four_or_more_reds(string):
    number_of_reds = 0
    for ch in string:
        if ch == "r":
            number_of_reds += 1
    if string == "":
        return False
    elif number_of_reds >= 4:
        return True
    else:
        return False

# -----------------------------------------------------------+
# function alternating_colors: Tests string if the colors
# red and blue are alternating
# -----------------------------------------------------------+
# string: the string used in the test
# -----------------------------------------------------------+

def alternating_colors(string):
    errors = 0
    for index in range(len(string)):
        x = string[index]
        if (index + 1) < int(len(string)):
            y = string[index+1]
            if x == y:
                errors += 1
            else:
                errors = errors
    if errors > 0 or string == "":
        return False
    else:
        return True

# --------------------------------------------------+
# manufactoria: The main function for Assignment 7. |
# --------------------------------------------------+

def manufactoria():

    # test strings to see if they contain four or more reds. 
    
    print("Testing four or more reds")
    print("---------------------------")
    test(four_or_more_reds, "")
    test(four_or_more_reds, "r")
    test(four_or_more_reds, "b")
    test(four_or_more_reds, "rbbbbbrbbbbbrbbbb")
    test(four_or_more_reds, "bbbbrbbbb")
    test(four_or_more_reds, "rbbrbbrr")  
    test(four_or_more_reds, "rrrrr")
    test(four_or_more_reds, "brrbrr")

    # test to see if strings contain alternating colors

    print()
    print("Testing alternating colors")
    print("--------------------------")

    # these tests should accept
    test(alternating_colors, "")
    test(alternating_colors, "r")
    test(alternating_colors, "rb")
    test(alternating_colors, "rbrbrbr")
    test(alternating_colors, "b")
    test(alternating_colors, "brbr")
    test(alternating_colors, "brbrbrbr")

    # these tests should not accept
    test(alternating_colors, "rr")
    test(alternating_colors, "bb")
    test(alternating_colors, "rbrbrrbr")
    test(alternating_colors, "brbbbr")

# -----------------------------------------------------------+
# test: Determine whether a given function accepts a string. |
# -----------------------------------------------------------|
# fn: The function to use, e.g. four_or_more_reds            |
# string: The string to test, e.g. "rrrbbb"                  |
# -----------------------------------------------------------+
    
def test(fn, string):

    if fn(string):
        result = "accepted"
    else:
        result = "not accepted"

    print('The string "' + string + '" is ' + result)

# -----------------------------------------------------------+

manufactoria()       # run the simulation 
