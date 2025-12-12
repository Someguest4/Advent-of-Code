result = 0
beams = set()
file = open("../inputs/7.txt")
first_time = True
for line in file:
    if first_time:
        beams.add(line.index("S"))
        first_time = False
    for i,char in enumerate(line):
        if char == "^" and i in beams:
            beams.remove(i)
            beams.add(i-1)
            beams.add(i+1)
            result += 1
print(result)