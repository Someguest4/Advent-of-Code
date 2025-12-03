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
    max_in_pack = find_max_in_range(0, len(pack) - 1, pack)
    #print("printing max in pack:"+ str(max_in_pack))
    max_after_max_in_pack = find_max_in_range(max_in_pack[1]+1,len(pack),pack)
    #print("printing max after max in pack:"+ str(max_after_max_in_pack))
    result += int(str(max_in_pack[0]) + str(max_after_max_in_pack[0]))

print(result)