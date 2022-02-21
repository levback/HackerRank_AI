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

def nextMove(x, y, color, grid):
    
    def flow_ink(i, k, color_index, color_name):
        if i < 0 or i >= len(actual_map):
            return
        if k < 0 or k >=len(actual_map[0]):
            return
        if actual_map[i][k] != color_name:
            return
        drop_ink(i, k, color_index)

    def drop_ink(i, k, color_index):
        if actual_ink_map[i][k] != 0:
            return 0
        actual_ink_map[i][k] = color_index
        if len(island_sets) == color_index - 1:
            island_sets.append(set())
        island_sets[color_index - 1].add((i, k))
        flow_ink(i + 1, k, color_index, actual_map[i][k])
        flow_ink(i - 1, k, color_index, actual_map[i][k])
        flow_ink(i, k + 1, color_index, actual_map[i][k])
        flow_ink(i, k - 1, color_index, actual_map[i][k])

        return 1

    def isneighbour(pos,island):
        for q in island:
            for i in ((1,0),(-1,0),(0,1),(0,-1)):
                if pos==(i[0]+q[0],i[1]+q[1]):
                    return True
        return False
    
    actual_map = grid
    m,n = len(grid),len(grid[0])
    actual_ink_map = [[0 for i in range(n)] for i in range(m)]
    island_sets = list()

    color_index = 1
    for i in range(m):
        for k in range(n):
            color_index = color_index + drop_ink(i,k, color_index)
            #print(actual_ink_map[i][k], end="")
        #print("")

    max_len = (0,0)
    click_to = (0,0)
    singleones = set()
    for x in island_sets:
        if len(x)==1:
            singleones.add(list(x)[0])
    for x in island_sets:
        singleonescount=0
        for i in singleones:
            if isneighbour(i,x):
                singleonescount+=1

        if len(x)>1 and max_len <= (singleonescount,len(x)) and actual_map[list(x)[0][0]][list(x)[0][1]] != "-":
            max_len = (singleonescount,len(x))
            click_to = list(x)[0]
        #print(x)

    print(str(click_to[0]) + " " + str(click_to[1]))

if __name__ == '__main__':
    x,y,k = [ int(i) for i in input().strip().split() ] 
    grid = [[i for i in str(input().strip())] for _ in range(x)] 
    nextMove(x, y, k, grid)
