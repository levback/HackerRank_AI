# A deterministic environment is one where the next state is completely 
# determined by the current state of the environment and the task 
# executed by the agent. If there is any randomness involved in 
# determining the next state, the environment is stochastic.
#
# The game Bot Clean took place in a deterministic environment. In this 
# version, the bot is given 200 moves to clean as many dirty cells as 
# possible. The grid initially has 1 dirty cell. When the bot cleans this
# cell, a new cell in the grid is made dirty. The new cell can be anywhere
# in the grid.
#
# The bot here is positioned at the top left corner of a 5*5 grid. Your 
# task is to move the bot to appropriate dirty cell and clean it.

# Link: https://www.hackerrank.com/challenges/botcleanr
# Developer : Levent Ozparlak

def nextMove(posr, posc, board):
    for i in range(5):
        for j in range(5):
            if board[i][j]=='d':
                dr,dc = i,j
                break
    
    if dr==posr and dc==posc:
        print("CLEAN")
    elif abs(dr-posr)>abs(dc-posc):
        print("UP") if dr<posr else print("DOWN")
    else:
        print("LEFT") if dc<posc else print("RIGHT")


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
