import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Peg Rectangle Solitaire    |
# Gage Hilyard                          |
# Last Modified: April 12, 2019         |
# ---------------------------------------
# Playable game of Rectangle Solitaire
# with a board size up to 9 x 9
# ---------------------------------------

# ---------------------------------------
# Start of PegRectangleSolitaire Class  |
# ---------------------------------------

class PegRectangleSolitaire:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " * |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

# ---------------------------------------
# Tests if there is one peg left.       |
# ---------------------------------------

    def game_won(self):
        count = 0
        num_rows, num_col = self.board.shape
        for x in range(num_rows):
            for y in range(num_col):
                if self.board[x][y] == True:
                    count+=1
        if count == 1:
            return True

# ---------------------------------------
# Tests if move is legal.               |
# ---------------------------------------

    def legal_move(self, row_start, col_start, row_end, col_end):
        #Tests if there is a peg
        if self.board[row_start][col_start] == True:
            #Tests Left Right Up Down Moves
            if row_start == row_end + 2 or row_start == row_end - 2:
                if col_start == col_end:
                    if self.board[row_end][col_end] == False:
                        return True
            elif col_start == col_end + 2 or col_start == col_end - 2:
                if row_start == row_end:
                    if self.board[row_end][col_end] == False:
                        return True
            #Tests Diagonal Moves
            if row_start == row_end + 2 or row_start == row_end - 2:
                if col_start == col_end -2 or col_start == col_end +2:
                    if self.board[row_end][col_end] == False:
                        return True

# ---------------------------------------
# Moves a peg and removes the one that  |
# got jumped.                           |
# ---------------------------------------        

    def make_move(self, row_start, col_start, row_end, col_end):
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True

        #Jumps Down
        if row_start == row_end - 2:
            if col_start == col_end:
                self.board[row_start+1][col_start] = False
        #Jumps Up
        if row_start == row_end + 2:
            if col_start == col_end:
                self.board[row_start-1][col_start] = False

        #Jumps Left         
        if col_start == col_end + 2:
            if row_start == row_end:
                self.board[row_start][col_start-1] = False

        #Jumps Right
        if col_start == col_end - 2:
            if row_start == row_end:
                self.board[row_start][col_start+1] = False
                
        #Jumps Down and Left
        if row_start == row_end - 2:
            if col_start == col_end + 2:
                self.board[row_start+1][col_start-1] = False
                
        #Jumps Up and Left
        if row_start == row_end + 2:
            if col_start == col_end + 2:
                self.board[row_start-1][col_start-1] = False

        #Jumps Up and Right
        if row_start == row_end + 2:
            if col_start == col_end -2:
                self.board[row_start-1][col_start+1] = False

        #Jumps Down and Right
        if row_start == row_end - 2:
            if col_start == col_end - 2:
                self.board[row_start+1][col_start+1] = False

# ---------------------------------------
# Sends final message according to pegs |
# left on the board.                    |
# ---------------------------------------

    def final_message(self):
        count = 0
        num_rows, num_col = self.board.shape
        for x in range(num_rows):
            for y in range(num_col):
                if self.board[x][y] == True:
                    count+=1
        print("Number of pegs left:", count)
        if count == 1:
            print("You're a genius!")
        if count == 2:
            print("You're pretty smart.")
        if count == 3:
            print("You're just average.")
        if count >= 4:
            print("You're just plain dumb.")

# ---------------------------------------
# End of PegRectangleSolitaire Class    |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Peg Rectangle Solitaire!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = PegRectangleSolitaire(rows, columns, row, column)
    print()

    keep_going = "yes"
    print(game)
    while (not game.game_won() and keep_going.lower() == "yes"):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is now allowed.")
        print()
        print(game)
        if not game.game_won():
            keep_going = input("Do you want to continue (yes or no): ")

    game.final_message()

# ---------------------------------------

main()
