boxes = []
distances = []
groups = []


def print_array(iterable):
    for line in iterable:
        print(line)


def Euclidean_distance(box1, box2):
    x1 = int(box1[0])
    y1 = int(box1[1])
    z1 = int(box1[2])
    x2 = int(box2[0])
    y2 = int(box2[1])
    z2 = int(box2[2])
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


def tuple_first_num(tuple):
    return tuple[0]


file = open("../inputs/8.txt")
for line in file:
    boxes.append(tuple(line.strip().split(",")))
# print_array(boxes)

for i in range(len(boxes)):
    box1 = boxes[i]
    for j in range(i + 1, len(boxes)):
        box2 = boxes[j]
        distances.append((Euclidean_distance(box1, box2), i, j))
distances.sort(key=tuple_first_num)
# print_array(distances[:10])
groups.append({distances[0][1], distances[0][2]})
for i in range(1, int(input("enter your range"))):
    found_in = []
    for j, group in enumerate(groups):
        if distances[i][1] in group or distances[i][2] in group:
            found_in.append(group)

    if not found_in:
        groups.append({distances[i][1], distances[i][2]})
    else:
        merged = {distances[i][1],distances[i][2]}
        for find in found_in:
            merged.update(find)
            groups.remove(find)
        groups.append(merged)



groups.sort(key=len, reverse= True)
print_array(groups)
result = 1
for i in range(3):
    result *= len(groups[i])

print(result)
