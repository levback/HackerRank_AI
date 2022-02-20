# Maze Escape is a popular 1 player game where a bot is trapped in 
# a maze and is expected to find its way out. In this version of 
# the game, 2 bots whose positions are not visible to each other 
# are placed at random points in the maze. the first bot to find 
# its way out of the maze wins the game.
#
# The visibility of the bot is restricted to its 8 adjacent cells as
# shown in the figure below
# 
# ---
# -b-
# ---
# where b is the bot. Bots can be facing any of the 4 directions. To 
# make this game more interesting, the orientation of both the bots 
# are randomly chosen at the start of the game and the map visible to
# them also changes according to the orientation.
#
# If the actual map is as shown below,
# 
# #######
# #--#-b#
# #--#--#
# #--#--#
# e-----#
# #-----#
# #######
# and your bot is positioned at (1,5) and is facing the RIGHT side of 
# the maze, the input will be
# ###
# #b-
# #--
# If your bot is facing UP, your input will be
# ###
# -b#
# --#
# If your bot is facing LEFT, your input will be
# --#
# -b#
# ###
# And if your bot is facing DOWN, your input will be
# #--
# #b-
# ###
# It is to be noted that your bot faces the direction in which it 
# chooses to make its next move.
#
# Input Format
#
# The walls are represented by character # ( ascii value 35), empty cells
# are represented by - (ascii value 45), the maze door which is the
# indication of the way out is represented by e (ascii value 101)
#
# The input contains 4 lines, the first line being the player id (1 or 2) 
# and followed by 3 lines, each line containing 3 of the above mentioned 
# characters which represents the 8 adjacent cells of the bot. The visible 
# maze given as input always has the bot at the center.
#
#Constraints
#
# 5 <= r,c <= 30 where r, c is the number of rows and columns of the maze.
# 
# Output Format
#
# Output UP, DOWN, LEFT or RIGHT which is the next move of the bot.

# Link: https://www.hackerrank.com/challenges/maze-escape
# Developer : Levent Ozparlak

import os
import math

def center_check(board):
    n = 4
    strings = ['UP','RIGHT','DOWN','LEFT']
    pattern = ''.join([''.join(b) for b in board])
    base_pattern = pattern.replace('e','#').replace('b','-')
    pcases = [['###--#--#',3],
              ['--#--#--#',0],
              ['-----#--#',0],
              ['--------#',0],
              ['###------',1],
              ['#--#--#--',0],
              ['####--#--',1],
              ['#--#--###',0]]
    
    centers = [board[0][1], board[1][2], board[2][1], board[1][0]]
    for i in range(n):
        if centers[i] in ['e']:
            return strings[i]
    for p,q in pcases:
        if p==base_pattern:
            return strings[q]
    return pattern
    
# Set next action the bot
def next_move(player, board):
    print(center_check(board))
    

# Start application
if __name__ == "__main__":
    # Set data
    player = int(input())
    board = [[j for j in input().strip()] for i in range(3)]  
    next_move(player, board)
