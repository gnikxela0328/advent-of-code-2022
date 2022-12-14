import re

# from bottom to top
stacks = [
    ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
    ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
    ['C', 'V', 'S', 'H'],
    [ 'H', 'F', 'G'],
    ['P', 'G', 'J', 'B', 'Z'],
    ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
    ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
    [ 'D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
    [ 'W', 'P', 'V', 'M', 'B', 'H']
]

def move_crates(stack_out, stack_in, count):
    for x in range(count):
        stack_in.append(stack_out.pop())

def move_crates_2(stack_out, stack_in, count):
    #print(stack_out)
    temp = []
    for x in range(count):
        temp.append(stack_out.pop())

    for x in temp[::-1]:
        stack_in.append(x)

def part_one(f):
    for x in f:
        move = re.split(r'move|from|to', x)[1:]
        count = int(move[0].strip())
        move_crates(stacks[int(move[1].strip()) - 1], stacks[int(move[2].strip()) - 1], count)

    for x in range(len(stacks)):
        print(stacks[x][-1])

def part_two(f):
    for x in f:
        move = re.split(r'move|from|to', x)[1:]
        count = int(move[0].strip())
        move_crates_2(stacks[int(move[1].strip()) - 1], stacks[int(move[2].strip()) - 1], count)

    for x in range(len(stacks)):
        print(stacks[x][-1])

if __name__ == "__main__":
    f = open('./data.txt', 'r')
    #part_one(f)
    part_two(f)
