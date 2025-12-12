file = open("../inputs/11.txt")

in_out_map = {

}
for line in file:
    line = line.strip().split(":")
    outputs = line[1].strip().split()
    in_out_map[line[0]] = outputs

print(in_out_map)

result = 0
queue = []
queue.append("you")
while queue:
    next = queue.pop()
    print("next", next)
    if next == "out":
        result += 1
    else:
        for item in in_out_map[next]:
            queue.append(item)
            print("appended: ", item)
print(result)