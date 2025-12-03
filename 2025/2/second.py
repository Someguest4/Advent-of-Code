result = 0
file = open("../inputs/2.txt")
def split_array_by_minus(element):
    return tuple(element.split("-"))
ids = file.readline().split(",")
ids =  list(map(split_array_by_minus,ids))
for start,end in ids:
    for i in range(int(start),int(end)+1):
        for j in range(2,len(str(i))+1):
            if len(str(i)) % j == 0:
                pattern_length = len(str(i)) // j
                juicy_slice = str(i)[:pattern_length]
                if juicy_slice*j == str(i):
                    result += i
                    break


print(result)