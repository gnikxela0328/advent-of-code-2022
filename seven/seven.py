class Folder():
    def __init__(self, name, parent):
        self.items = []
        self.size = 0
        self.parent = parent
        self.name = name

"""
Idea - create class instance of each folder which describes their items, then traverse tree and add to total at each level that satisfies requirement

1) arraange items into tree structure by iterating through input and sort accordingly

2) traverse tree, dfs, add to total when all items in the folder are less than 100,000

3) if a folder is encountered, the traversal will follow the path downwards until bottom is reached

4) total will be calculated using bottom up approach
"""


def part_one(f):

    root = Folder(name="/", parent=None)
    current_node = root


    ### TREE CREATION
    for x in f:

        ## Interpret terminal lines
        command = x.split(" ")

        # command
        if command[0] == "$":

            # changing to a new folder, set current node to selected folder
            if command[1] == "cd":
                if command[2].strip() == "..":
                    #print("switched node to parent " + current_node.parent.name)
                    current_node = current_node.parent
                else:
                    for y in current_node.items:
                        if y.name == command[2]:
                            #print("switched node to " + command[2])
                            current_node = y
            
            # listing directories, this will happen at each level, not sure what to do with this one
            elif command[1] == "ls":
                print()

        # directory found, create a new node and store it in items list
        elif command[0] == "dir":
            current_node.items.append(Folder(name=command[1], parent=current_node))

        # file found, add size to node 
        else:
            current_node.size+=int(command[0])


    folder_totals = traverse_tree_one(root)
    print(folder_totals)

def part_two(f):
    root = Folder(name="/", parent=None)
    current_node = root


    ### TREE CREATION
    for x in f:

        ## Interpret terminal lines
        command = x.split(" ")

        # command
        if command[0] == "$":

            # changing to a new folder, set current node to selected folder
            if command[1] == "cd":
                if command[2].strip() == "..":
                    #print("switched node to parent " + current_node.parent.name)
                    current_node = current_node.parent
                else:
                    for y in current_node.items:
                        if y.name == command[2]:
                            #print("switched node to " + command[2])
                            current_node = y
            
            # listing directories, this will happen at each level, not sure what to do with this one
            elif command[1] == "ls":
                print()

        # directory found, create a new node and store it in items list
        elif command[0] == "dir":
            current_node.items.append(Folder(name=command[1], parent=current_node))

        # file found, add size to node 
        else:
            current_node.size+=int(command[0])


    folder_totals = traverse_tree_two(root)
    print(folder_totals)

def traverse_tree_one(root):

    
    if len(root.items) > 0:
        for x in root.items:
            root.size+= traverse_tree_one(x)

    
    if root.size < 100000:
        print(root.size)
        
    return root.size

def traverse_tree_two(root):
    if len(root.items) > 0:
        for x in root.items:
            root.size+= traverse_tree_two(x)

    
    if root.size >= 4795667:
        print(root.size)
    #print(root.size)
        
    return root.size


if __name__ == "__main__":
    f = open('./data.txt', 'r')
    #part_one(f)

    # find 4795667
    part_two(f)