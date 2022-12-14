"""
Idea - make a bidirectional pass at each row and compare each tree to the running local maximum. If it is less than or equal, the tree is hidden. start horizontal, then search vertical

1) pass forwards through list, find local max. If greater than max, mark visible and update max

2) reset max and repeat from other direction

3) store each visible tree in set

4) redo search for verticals, this time filtering by the marked coordinates

5) return length of set
"""

def part_one(f):
    data = []
    for x in f:
        data.append(list(x.strip()))
    
    # visible tree coordinates (x,y)
    visible_trees = set()

    # search rows forward and back
    for x in range(len(data)):

        # search forwards
        local_max = -1

        for y in range(len(data[x])):
            if int(data[x][y]) > local_max:
                local_max = int(data[x][y])
                visible_trees.add(tuple((x,y)))
        
        # search backwards
        local_max = -1

        for idy, y in reversed(list(enumerate(data[x]))):
            if int(data[x][idy]) > local_max:
                local_max = int(data[x][idy])
                visible_trees.add(tuple((x,idy)))

    print(visible_trees)
    
    # search columns up and down
    for x in range(len(data[0])):
        
        # search down
        local_max = -1

        for y in range(len(data)):
            if ((x,y)) not in visible_trees:
                if int(data[x][y]) > local_max:
                    local_max = int(data[x][y])
                    visible_trees.add(tuple((x,y)))

        
        # search up
        local_max = -1

        for y in reversed(range(len(data)-1)):
            if (x,y) not in visible_trees:
                if int(data[x][y]) > local_max:
                    local_max = int(data[x][y])
                    visible_trees.add(tuple((x,y)))

    #print(len(visible_trees.sort(key=lambda x: x[0])))
    

    

def part_two(f):
    print()

if __name__ == "__main__":
    f = open('./data.txt', "r")
    part_one(f)
    #part_two(f)
