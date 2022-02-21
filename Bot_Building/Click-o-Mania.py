# Clickomania is a 1-player game consisting of a rectangular grid of square blocks, 
# each colored in one of k colors. Adjacent blocks horizontally and vertically of 
# the same color are considered to be a part of the same group. A move selects a 
# group containing at least two blocks and removes those blocks, followed by two 
# "falling" rules;
#
# Any blocks remaining above the holes created, fall down through the same column.
# Any empty columns are removed by sliding the succeeding columns left.

# Link: https://www.hackerrank.com/challenges/click-o-mania
# Developer : Levent Ozparlak

#!/bin/python
def connected(grid,cmap):
    cntr = 0
    m,n = len(grid),len(grid[0])
    for i in range(m-1,-1,-1):
        for j in range(n):
            if grid[i][j] != '-':
                if i==m-1:
                    if j == 0:
                        cmap[i][j] = cntr
                        cntr += 1
                    elif grid[i][j]==grid[i][j-1]:
                        cmap[i][j] = cmap[i][j-1]
                    else:
                        cmap[i][j] = cntr
                        cntr += 1
                else:
                    if j == 0:
                        if grid[i][j]==grid[i+1][j]:
                            cmap[i][j] = cmap[i+1][j]
                        else:
                            cmap[i][j] = cntr
                            cntr +=1
                    else:
                        if grid[i][j]==grid[i+1][j] and grid[i][j]==grid[i][j-1]:
                            if cmap[i][j-1] != cmap[i+1][j]:
                                t = cmap[i][j-1]
                                u = cmap[i+1][j]
                                for k in range(m-1,i-1,-1):
                                    for l in range(n):
                                        if cmap[k][l]==t:
                                            cmap[k][l] = u
                            else:
                                cmap[i][j] = cmap[i][j-1]
                        elif grid[i][j]==grid[i+1][j]:
                            cmap[i][j] = cmap[i+1][j]
                        elif grid[i][j]==grid[i][j-1]:
                            cmap[i][j] = cmap[i][j-1]
                        else:
                            cmap[i][j] = cntr
                            cntr += 1
    return cmap
                        
def stats(cmap,grid):
    vals = dict()
    for i in range(len(cmap)):
        for j in range(len(cmap[i])):
            if grid[i][j]!= '-':
                try:
                    vals[cmap[i][j]] +=1
                except:
                    vals[cmap[i][j]] = 0
    maxv = 0
    key = None
    for k in vals.keys():
        c = vals[k]
        if k!=-1 and maxv<c:
            maxv = c
            key = k
    for i in range(len(cmap)):
        for j in range(len(cmap[i])):
            if cmap[i][j] == key:
                if grid[i][j] == '-':
                    print(maxv,key)
                return i,j
    
            
        
    
def nextMove(x, y, color, grid):
    cmap = [[-1 for j in range(y)] for i in range(x)]
    cmap = connected(grid,cmap)
    #print(grid[0])
    #print(cmap[0])
    #for c in cmap:
    #    print(c)
    xx,yy = stats(cmap,grid)
    print(xx,yy)

if __name__ == '__main__':
    x,y,k = [ int(i) for i in input().strip().split() ] 
    grid = [[i for i in str(input().strip())] for _ in range(x)] 
    nextMove(x, y, k, grid)
