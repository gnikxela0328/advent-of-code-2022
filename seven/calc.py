f = open("./printed_results_one.txt", "r")

total = 0

for x in f:
    total+=int(x)

print(total)

g = open('./printed_results_two.txt', 'r')

two = []

for x in g:
    two.append(int(x))

two.sort()
print(two[0])