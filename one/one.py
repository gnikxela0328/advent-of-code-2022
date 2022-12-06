def part_one(f):
    elves = []
    temp = []


    for x in f:
        if x == "\n" or x == None:
            elves.append(temp)
            temp = []
        else:
            temp.append(x)

    max_num = 0

    for x in elves:
        temp = 0
        for y in x:
            temp += int(y)

        max_num = max(temp, max_num)

    print(max_num)

def part_two(f):
    elf_totals = []
    elves = []
    temp_list = []

    # group elves
    for x in f:
        if x == "\n" or x == None:
            elves.append(temp_list)
            temp_list = []
        else:
            temp_list.append(x)


    # sum each elf
    for x in elves:
        temp_count = 0
        for y in x:
            temp_count += int(y)

        elf_totals.append(temp_count)

    
    elf_totals.sort()
    #print(elf_totals)

    print(elf_totals[-1] + elf_totals[-2] + elf_totals[-3])

if __name__ == "__main__":
    f = open("/Users/ranger/Documents/code/advent-of-code/one/data.txt", "r")

    # test one or the other. Otherwise file buffer will run through entire
    # file and not leave any data to be parsed

    #part_one(f)
    part_two(f)