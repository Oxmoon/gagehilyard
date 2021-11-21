def legal_play(first_value, first_color, second_value, second_color):
    if(first_value == second_value):
        return True
    elif(first_color == second_color):
        return True
    else:
        return False

def legal_play2(first_value, first_color, second_value, second_color):
    if(first_value == second_value) or (first_color == second_color):
        return True
    else:
        return False

def legal_play3(first_value, first_color, second_value, second_color):
    return (first_value == second_value) or (first_color == second_color)

print(legal_play3(3, "blue", 3, "green"))
print(legal_play3(5, "yellow", 7, "yellow"))
print(legal_play3(9, "red", 6, "green"))
