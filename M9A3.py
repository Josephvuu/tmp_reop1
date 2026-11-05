# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 9 Assignment 3

def print_board(board):
    n = len(board)
    div = '-' * (2 * n + 1)
    print(div)
    for row in board:
        print('|' + '|'.join(row) + '|')
    print(div)

board1_list = [['*','*','*'], ['*','+','*'], ['*','*','*']]
print_board(board1_list)
print()

board2_list = [['*',' ',' ','*'], 
              ['*',' ',' ','*'], 
              ['*',' ',' ','*'], 
              ['*',' ',' ','*']]
print_board(board2_list)
print()

board3_list = [['*',' ','*',' ','*'], 
              [' ','*',' ','*',' '], 
              [' ',' ',' ',' ',' '], 
              [' ','+',' ','+',' '], 
              ['+',' ','+',' ','+']]
print_board(board3_list)