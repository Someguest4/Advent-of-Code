result = 0
file = open("../inputs/2.txt")
def split_array_by_minus(element):
    return tuple(element.split("-"))
ids = file.readline().split(",")
ids =  list(map(split_array_by_minus,ids))
for start,end in ids:
    for i in range(int(start),int(end)+1):
        if len(str(i)) % 2 == 0:
            half = len(str(i)) // 2
            if str(i)[:half] == str(i)[half:]:
                result += i
print(result)