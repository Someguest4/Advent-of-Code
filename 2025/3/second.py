result = 0
file = open("../inputs/3.txt")
packs = []
for line in file:
    packs.append(line.strip())
#print(packs)


def find_max_in_range(start, end, pack):
    max_in_range = (0, 0)
    for i in range(start, end):
        num = int(pack[i])
        if num > max_in_range[0]:
            max_in_range = (num, i)
    return max_in_range


for pack in packs:
    maxes_in_pack = ""
    previous_max_in_pack_position = -1
    for i in range(0,12):
        maximum = find_max_in_range(previous_max_in_pack_position+1,len(pack)-(11-i),pack)
        maxes_in_pack += str(maximum[0])
        previous_max_in_pack_position = maximum[1]
    print(maxes_in_pack)
    result += int(maxes_in_pack)
print("result: " + str(result))