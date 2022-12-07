def part_one(f):
    total = 0

    for x in f:
        left = x[:int(len(x) / 2)]
        right = x[int(len(x)/2):]

        letter = ""
        val = 0

        for y in left:
            if y in right:
                letter = y
                break
        
        if letter.isupper():
            val = ord(letter) - 38
        else:
            val = ord(letter) - 96
        
        total += val
    
    print(total)

def part_two(f):
    groups = []
    temp = []
    total = 0

    for x in f:
        if len(temp) < 3:
            temp.append(x.strip())
        else:
            #print("add to group")
            temp.sort(key=lambda x: len(x))
            groups.append(temp)
            temp = []
            temp.append(x.strip())
    
    groups.append(temp)
    print(groups)
    #print(len(groups))
    for x in groups:
        letter = ""
        val = 0
        for y in x[0]:
            if y in x[1] and y in x[2]:
                letter = y
                break
        
        if letter.isupper():
            val = ord(letter) - 38
        else:
            val = ord(letter) - 96
        
        total += val
        
    print(total)



if __name__ == "__main__":
    f = open('data.py', "r")
    #part_one(f)
    part_two(f)