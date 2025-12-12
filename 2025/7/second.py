result = 0



file = open("../inputs/7.txt")
line = file.readline()
beams = [0] * len(line)
beams[line.index("S")] = 1

for line in file.readlines():

    for i,char in enumerate(line):
        if char == "^" and beams[i] > 0:
            if i-1 >= 0:
                beams[i-1] += beams[i]
            if i+1 < len(line):
                beams[i+1] += beams[i]
            beams[i] = 0
print(sum(beams))