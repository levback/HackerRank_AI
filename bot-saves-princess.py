# Princess Peach is trapped in one of the four corners of a square grid. 
# You are in the center of the grid and can move one step at a time in 
# any of the four directions. Can you rescue the princess?

# Complete the function displayPathtoPrincess which takes in two 
# parameters - the integer N and the character array grid. The grid 
# will be formatted exactly as you see it in the input, so for the 
# sample input the princess is at grid[2][0]. The function shall output 
# moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach 
# the princess. The goal is to reach the princess in as few moves as possible.

# Link: https://www.hackerrank.com/challenges/saveprincess
# Developer : Levent Ozparlak


def displayPathtoPrincess(n,grid):
#print all the moves here
    r,c = int((n-1)/2),int((n-1)/2)
    corners = ((0,0),(0,n-1),(n-1,0),(n-1,n-1))
    for cc in corners:
        if grid[cc[0]][cc[1]] == 'p':
            p_r,p_c = cc
            break
    dr, dc = p_r - r, p_c - c
    rtx = ("UP\n","DOWN\n")
    ctx = ("LEFT\n","RIGHT\n")
    ftx = (rtx[int(dr>0)]+ctx[int(dc>0)])*abs(dr)
    print(ftx)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
