def part_one(f):
    data = []
    for x in f:
        data.append(list(x.strip()))
    
    print(data)
    

def part_two(f):
    print()

if __name__ == "__main__":
    f = open('./data.txt', "r")
    part_one(f)
    #part_two(f)
