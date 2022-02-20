# The game Bot Clean took place in a fully observable environment, i.e., 
# the state of every cell was visible to the bot at all times. Let us 
# consider a variation of it where the environment is partially observable. 
# The bot has the same actuators and sensors. But the sensors visibility is
# confined to its 8 adjacent cells.

# Link : https://www.hackerrank.com/challenges/botcleanv2
# Developer : Levent Ozparlak

#!/usr/bin/python3
from os.path import isfile, dirname
from os import makedirs
import math

# Get board data from saved cache
def get_info_file():
    open_board = []
    fn = "temp/board.txt"
    if isfile(fn):
        with open(fn, "r") as f:
            board_text = f.read().split('\n')
            for i in range(len(board_text)):
                temp_row = []
                for j in range(len(board_text[i])):
                    temp_row.append(board_text[i][j])
                open_board.append(temp_row)
    return open_board

# Save the board into file cache
def save_info_file(board, fn):
    makedirs(dirname(fn), exist_ok=True)
    with open(fn, "w") as f:
        for i in range(len(board)):
            columns = "\n" if i > 0 else ""
            for j in range(len(board[i])):
                if board[i][j] == "b":
                    columns = columns + "-"
                else:    
                    columns = columns + board[i][j]
            f.write(columns)

# Save and read the file that contains the bot's memory
def update_info_file(board):
    fn = "temp/board.txt"
    if isfile(fn):
        with open(fn, "r") as f:
            new_open_board = []
            open_board = f.read().split('\n')
            for i in range(len(open_board)):
                new_row = []
                for j in range(len(open_board[i])):
                    if ((open_board[i][j] == 'o' and board[i][j] == '-') or 
                        (open_board[i][j] == 'd' and board[i][j] == '-') or
                        (open_board[i][j] == 'd' and board[i][j] == 'b')):
                        new_row.append('-')
                    elif open_board[i][j] == 'o' and board[i][j] == 'd':
                        new_row.append('d')
                    else:
                        new_row.append(open_board[i][j])
                new_open_board.append(new_row)
            save_info_file(new_open_board, fn)
    else:
        save_info_file(board, fn)
            

# Euclidean Distance
def dist(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

# Find certain elements on the board
def get_element_board(board, pos, element):
    dirties = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in element:
                dirties.append([i, j, dist(pos,[i,j])])
    return dirties

# Set next action the bot
def next_move(posx, posy, board):
    # Save board in bot's memory  
    update_info_file(board)
    elements = get_element_board(board, [posx,posy], ['d'])
    if len(elements) == 0:
        elements = get_element_board(get_info_file(), [posx,posy], ['o','d'])

    elements.sort(key=lambda x:x[2])
    
    if (len(elements) > 0):
        if elements[0][1]  > posy:
            print('RIGHT')
        elif elements[0][1] < posy:
            print('LEFT')
        elif elements[0][0] < posx:
            print('UP')
        elif elements[0][0] > posx:
            print('DOWN')
        else:
            print('CLEAN')
                

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)
