# Battleship is a popular 2 player game that takes place on a 10 x 10 board. Ships of 
# various sizes are placed on the 10 x 10 board either horizontally or vertically. 
# The position of the ships are hidden to the user. Your task is to sink all the ships.
#
#Ships of the following size are given to each player.
#
# - Submarine (1 x 1) - 2 units
# - Destroyer (2 x 1) - 2 units
# - Cruiser (3 x 1) - 1 unit
# - Battleship(4 x 1) - 1 unit
# - Carrier (5 x 1) - 1 unit
# In this version of the game, you will be playing solo. A testcase has a configuration 
# of ship positions and your task is to destroy all the ships using the minimum number 
# of moves.

# Link: https://www.hackerrank.com/challenges/battleship1p
# Developer : Levent Ozparlak

import random
def search(x,y,grid,v = 'd'):
    g_row = grid[x]
    g_col = [grid[i][y] for i in range(len(grid))]
    strpy = y
    endpy = y+1
    brdr = len(g_row)-1
    for i in range(y+1,brdr+1):
        if g_row[i]!=v:
            endpy = i
            break
        elif i==brdr:
            endpy = brdr+1
            break
    strpx = x
    endpx = x+1
    brdr = len(g_col)-1
    for i in range(x+1,brdr+1):
        if g_col[i]!=v:
            endpx = i
            break
        elif i == brdr:
            endpx == brdr+1
            break        
    return (endpx-strpx,endpy-strpy),((strpx,strpy),(endpx,endpy))  
def hsearch(x,y,grid,v='h'):
    g_row = grid[x]
    g_col = [grid[i][y] for i in range(len(grid))]
    ru_h = 0
    cu_h = 0
    rd_h = 0
    cd_h = 0
    brdr = len(g_row)-1
    for i in range(y+1,brdr+1):
        if g_row[i]!=v:
            rd_h = i-y
            break
        elif i==brdr:
            rd_h = i-y
            break
    brdr = 0
    for i in range(y-1,brdr-1,-1):
        if g_row[i]!=v:
            ru_h = y-i
            break
        elif i == brdr:
            ru_h = y-i
            break
    brdr = len(g_col)-1
    for i in range(x+1,brdr+1):
        if g_col[i]!=v:
            cd_h = i-x
            break
        elif i==brdr:
            cd_h = i-x
            break
    brdr = 0
    for i in range(x-1,brdr-1,-1):
        if g_col[i]!=v:
            cu_h = x-i
            break
        elif i==brdr:
            cu_h = x-i
            break
    return [ru_h,cu_h,rd_h,cd_h]
    
    
def nextMove(n,grid):
    dlist = {2:2,3:1,4:1,5:1}
    cgrid = [[x for x in g] for g in grid] 
    for i in range(n):
        for j in range(n):
            if cgrid[i][j] == 'd':
                t,clr = search(i,j,cgrid)
                #print(t)
                dlist[max(t)] -=1
                for k in range(clr[0][0],clr[1][0]):
                    for l in range(clr[0][1],clr[1][1]):
                        cgrid[k][l] = 'x'
    candids = []
    maxp = 0
    for i in range(n):
        for j in range(n):
            if cgrid[i][j] == '-':
                t = hsearch(i,j,cgrid,v='-')
                p = 0
                for k in range(2,min(6,t[0])):
                    row_ext = min(k-1,t[0])+min(k-1,t[2])+1
                    p += dlist[k]*(row_ext-k+1)
                for k in range(2,min(6,t[1])):
                    col_ext = min(k-1,t[1])+min(k-1,t[3])+1
                    p += dlist[k]*(col_ext-k+1) 
                tt = hsearch(i,j,cgrid)    
                
                p += 100*max(tt)
                if p > maxp:
                    maxp = p
                candids.append([i,j,p])                
    #print(candids)
    mcands =[]
    for [i,j,t] in candids:
        if t == maxp:
            mcands.append([i,j])
    if len(mcands)>1:
        r = int(len(mcands)*random.random())
        print(mcands[r][0],mcands[r][1])
    else:
        print(mcands[0][0],mcands[0][1])
        
if __name__ == '__main__':
    n = int(input())
    grid = [[i for i in str(input().strip())] for _ in range(n)] 
    nextMove(n, grid)
