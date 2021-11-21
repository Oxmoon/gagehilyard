# Practicum 3

# Question 1
 
##def more_reds(string):
##    number_of_reds = 0
##    number_of_blues = 0
##    for ch in string:
##        if ch == "r":
##            number_of_reds += 1
##        if ch == "b":
##            number_of_blues += 1
##    if string == "":
##        return False
##    elif number_of_reds > number_of_blues:
##        return True
##    else:
##        return False

# Question 2

##import random
##
##def random_average(low, high, how_many):
##    total = 0
##    for i in range(0, how_many):
##        number = random.randrange(low, high)
##        total += number
##    average = (total / how_many)
##    print(average)

# Question 3

##print("Let's begin our conversation!")
##words = ""
##while words.lower() != "can we end this conversation now?":
##    words = input("Talk to me: ")

# Question 4

def merge_words(word_1, word_2, merged_words =""):
    if word_1 == "" and word_2 == "":
        print(merged_words)
    elif len(merged_words) % 2 == 0 and word_1 != "":
        ch = word_1[0]
        merge_words(word_1.replace(ch,"", 1), word_2, (merged_words + ch))
    elif word_2 != "":
        ch = word_2[0]
        merge_words(word_1, word_2.replace(ch, "", 1), (merged_words + ch))

merge_words("aaa", "bbb")
merge_words("dog", "cat")
merge_words("big", "small")

