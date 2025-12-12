file = open("../inputs/11.txt")

in_out_map = {

}
for line in file:
    line = line.strip().split(":")
    outputs = line[1].strip().split()
    in_out_map[line[0]] = outputs

#print(in_out_map)
result = 0
def find_paths(path,current):
    path.add(current)
    global result
    #print("current: " , current)
    #print("path: ", path)
    if current == "out":
        if "dac" in path and "fft" in path:
            result += 1
        return

    else:
        for child in in_out_map[current]:
            child_path = path.copy()
            find_paths(child_path,child)

find_paths(set(),"svr")
print(result)