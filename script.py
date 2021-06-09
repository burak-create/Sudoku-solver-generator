import numpy as np
from random import randint, shuffle
import sys
"""
test_board = [
        [4, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 8, 2, 7],
        [8, 0, 0, 4, 1, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 3, 0, 0, 0, 0, 4, 0, 6],
        [0, 0, 0, 0, 9, 6, 2, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 5, 0]
        ]
"""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# An empty 2D array to generate sudoku puzzle
def empty_grid():
    global board
    board = [[0 for x in range(9)] for y in range(9)]
    generate()

# Function which is checking possiblety of values
def poss(colm, row, value):
    for i in range(0, 9):
        if board[colm][i] == value or board[i][row] == value:
            return False
    row0 = (row // 3)*3
    colm0 = (colm // 3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[colm0+i][row0+j] == value:
                return False
    return True

# A recursive/backtracking function to generate a 9x9 sudoku puzzle
def generate():
    # Find the empty boxes and fill them with the possible numbers
    for colm in range(9):
        for row in range(9):
            if board[colm][row] == 0:
                shuffle(number_list)
                for value in  number_list:
                    if poss(colm, row, value):
                        board[colm][row] = value
                        generate()
                        board[colm][row] = 0
                return
    game_mode()

def remover(remove):
    while remove >= 0:
        remove -= 1
        print(remove)
        row = randint(0, 8)
        colm = randint(0, 8)
        while board[row][colm] == 0:
            row = randint(0, 8)
            colm = randint(0, 8)
        board[row][colm] = 0
    printer()

def printer():
    print(np.matrix(board))
    sys.exit()

# E = 20 
# M = 30
# H = 40
# Expert = 50
def game_mode():
    if val == "1" or val == "easy":
        remover(20)
    elif val == "2" or val == "medium":
        remover(30)
    elif val == "3" or val == "hard":
        remover(40)
    elif val == "4" or val == "expert":
        remover(50)



"""
# A recursive/backtracking function to solve a 9x9 sudoku puzzle
def solve():
    for colm in range(9):
        for row in range(9):
            if board[colm][row] == 0:
                for value in  range(1, 10):
                    if poss(colm, row, value):
                        board[colm][row] = value
                        solve()
                        board[colm][row] = 0
                return
    print(np.matrix(board))
"""

# A function for take user input for game difficulty
def choice():
    global val
    print("\n\nWelcome to Sudoku Generator!\n\n")
    start_the_game = input("Do you want to start the game?(y/n)\n\n").lower()
    if start_the_game == ("y"):
        val = input("""
        1) Easy
        2) Medium
        3) Hard
        4) Expert\n\n
""").lower()
        if int(val) >= 1 and int(val) < 5:
            empty_grid()
        else:
            print("Invalid choice")
    else:
        sys.exit()



if __name__ == '__main__':
    remove = 0
    choice()
    