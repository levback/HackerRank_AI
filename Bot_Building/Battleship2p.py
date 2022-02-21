# Battleship is a popular 2-player game that takes place a 10 x 10 board. Ships 
# of various sizes are placed on the 10 x 10 board either horizontally or 
# vertically. The position of the ships are hidden to the user. Your task is to 
# sink all the ships.
#
# Ships of the following size are given to each player.
# 
# Submarine (1 x 1) - 2 nos
# Destroyer (2 x 1) - 2 nos
# Cruiser (3 x 1) - 1 nos
# Battleship(4 x 1) - 1 nos
# Carrier (5 x 1) - 1 nos
# In this version of the game, you will initially specify the positions of your 
# ships in a specific format and then start attacking the positions of your opponent.

# Link : https://www.hackerrank.com/challenges/battleship
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
    dlist = {1:2,2:2,3:1,4:1,5:1}
    cgrid = [[x for x in g] for g in grid] 
    for i in range(n):
        for j in range(n):
            if cgrid[i][j] == 'd':
                t,clr = search(i,j,cgrid)
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
                for k in range(1,min(6,t[0])):
                    row_ext = min(k-1,t[0])+min(k-1,t[2])+1
                    p += dlist[k]*(row_ext-k+1)
                for k in range(1,min(6,t[1])):
                    col_ext = min(k-1,t[1])+min(k-1,t[3])+1
                    p += dlist[k]*(col_ext-k+1) 
                tt = hsearch(i,j,cgrid)    
                
                p += 100*max(tt)
                if p > maxp:
                    maxp = p
                candids.append([i,j,p])                
    mcands =[]
    for [i,j,t] in candids:
        if t == maxp:
            mcands.append([i,j])
    if len(mcands)>1:
        r = int(len(mcands)*random.random())
        print(mcands[r][0],mcands[r][1])
    else:
        print(mcands[0][0],mcands[0][1])

def csearch(direction,grid,size):
    candids = []
    if direction == 0:
        for i in range(len(grid)):
            gp = grid[i]
            for j in range(len(gp)-size+1):
                if gp[j] == '-':
                    for k in range(j+1,len(gp)):
                        if gp[k]!='-':
                            tt = k
                            break
                        elif k == len(gp)-1:
                            tt = k
                    #print(tt)
                    if tt-j>=size:
                        candids.append([i,j,i+1,j+size])
    else:
        for i in range(len(grid[0])):
            gp = [grid[k][i] for k in range(len(grid))]
            for j in range(len(gp)-size):
                if gp[j] == '-':
                    for k in range(j+1,len(gp)):
                        if gp[k]!='-':
                            tt = k
                            break
                        elif k == len(gp)-1:
                            tt = k
                    #print(tt)
                    if tt-j>=size:
                        candids.append([i,j,i+size,j+1])
    return candids

def pick_ship(grid, size):
    coin = int(2*random.random())
    candids = csearch(coin,grid,size)
    t = int(len(candids)*random.random())
    #print(candids,t)
    pos = candids[t]
    for i in range(pos[0],pos[2]):
        for j in range(pos[1],pos[3]):
            grid[i][j] = 'x'
    return grid,pos
def initialize():
    dlist = {1:2,2:2,3:1,4:1,5:1}
    n = 10
    grid = [['-' for _ in range(n)] for _ in range(n)]
    # Carrier
    grid, carr_pos = pick_ship(grid,5)
    # Battleship
    grid, batt_pos = pick_ship(grid,4)
    # Cruiser
    grid, crui_pos = pick_ship(grid,3)
    # Destroyer 1
    grid, des1_pos = pick_ship(grid,2)
    # Destroyer 2 
    grid, des2_pos = pick_ship(grid,2)
    # Submarine 1
    grid, sub1_pos = pick_ship(grid,1)
    # Submarine 2
    grid, sub2_pos = pick_ship(grid,1)
    
    print('{0:d} {1:d}'.format(sub1_pos[0],sub1_pos[1]))
    print('{0:d} {1:d}'.format(sub2_pos[0],sub2_pos[1]))
    print('{0:d} {1:d}:{2:d} {3:d}'.format(des1_pos[0],des1_pos[1],des1_pos[2]-1,des1_pos[3]-1))
    print('{0:d} {1:d}:{2:d} {3:d}'.format(des2_pos[0],des2_pos[1],des2_pos[2]-1,des2_pos[3]-1))
    print('{0:d} {1:d}:{2:d} {3:d}'.format(crui_pos[0],crui_pos[1],crui_pos[2]-1,crui_pos[3]-1))
    print('{0:d} {1:d}:{2:d} {3:d}'.format(batt_pos[0],batt_pos[1],batt_pos[2]-1,batt_pos[3]-1))
    print('{0:d} {1:d}:{2:d} {3:d}'.format(carr_pos[0],carr_pos[1],carr_pos[2]-1,carr_pos[3]-1))
    
    
if __name__ == '__main__':
    kk = input()
    if kk.startswith('INIT'):
        initialize()
    else:
        n = int(kk)
        grid = [[i for i in str(input().strip())] for _ in range(n)] 
        nextMove(n, grid)
