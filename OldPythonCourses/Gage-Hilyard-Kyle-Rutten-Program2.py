# -----------------------------------------+
# Gage Hilyard and Kyle Rutten             |
# CSCI 127, Program 2                      |
# Last Updated: Jan 31, 2019               |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+


# flush, pair, and fifteen will return score values
def flush(suit_list):
    counter = 0
    for i in range(len(suit_list)):
        if suit_list[0] == suit_list[i]:
            counter +=1
    if counter == 5:
        return 5
    else:
        return 0

def pair(card_list):
    counter = 0
    for i in range(len(card_list)):
        for j in range(i+1, len(card_list)):
            if card_list[i] == card_list[j]:
                counter += 2
    return counter
        

def fifteen(cards):
    return 0

def print_hand(cards, number):
    pass

def evaluate_hand(hand_as_list):
    card_list = []
    suit_list = []
    number_list = []
    for i in range(len(hand_as_list)):
        card_list.append(hand_as_list[i][0])
        suit_list.append(hand_as_list[i][1])
    print("Points scored: " +(str(flush(suit_list) + pair(card_list) + fifteen(number_list))))
    
# translate and print score through calling
# the flush, pair and fifteen funcitons

# -----------------------------------------+
# Do not change anything below this line.  |
# -----------------------------------------+

def process_hands(cribbage_input, cards_in_hand):
    number = 1
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0].capitalize(), hand[1].capitalize()])
            hand = hand[2:]
        print_hand(hand_as_list, number)
        evaluate_hand(hand_as_list)
        number += 1

# -----------------------------------------+

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 5)
    cribbage_file.close()

# -----------------------------------------+

main()
