def part_one(f):
    # find larger pair
    # compare left and right numbers
    total_count = 0

    for x in f:
        ranges = x.split(",")
        left = ranges[0].split("-")
        right = ranges[1].strip().split("-")

        ldiff = abs(int(left[0]) - int(left[1]))
        rdiff = abs(int(right[0]) - int(right[1]))

        if ldiff >= rdiff:
            if int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[1]):
                total_count+=1
        else:
            if int(left[0]) >= int(right[0]) and int(left[1]) <= int(right[1]):
                total_count+=1
        
    print(total_count)


def part_two(f):
    total_count = 0

    for x in f:
        ranges = x.split(",")
        left = ranges[0].split("-")
        right = ranges[1].strip().split("-")
        print("---")


        if (int(left[0]) <= int(right[1]) and int(left[0]) >= int(right[0])) or (int(left[1]) >= int(right[0]) and int(left[0]) <= int(right[0])):
            #print(left)
            #print(right)
            total_count+=1
        else:
            print(left)
            print(right)
        
    print(total_count)

if __name__ == "__main__":
    f = open("data.txt", "r")

    # test one or the other. Otherwise file buffer will run through entire
    # file and not leave any data to be parsed

    #part_one(f)
    part_two(f)