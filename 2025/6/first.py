final_result = 0
grid = []
file = open("../inputs/6.txt")
lines = file.readlines()

def print_grid(grid):
    for row in grid:
        print(row)

def add(iterable):
    result = 0
    for num in iterable:
        result += int(num)
    print("add result: ", result)
    return result

def mul(iterable):
    result = 1
    for num in iterable:
        result *= int(num)
    print("mul result: ",result)
    return result

for line in lines:
    dirty_row = line.strip().split(" ")
    row=[]
    for i in range(len(dirty_row)):
        if  dirty_row[i] != "":
            row.append(dirty_row[i])
    grid.append(row)

print_grid(grid)
for i in range(len(grid[0])):
        nums = []
        print("l",len(grid[0]))
        operation = grid[len(grid)-1][i]

        for j in range(len(grid)-1):


            nums.append(grid[j][i])

        print(nums)
        if operation == "+":
            final_result += add(nums)
        elif operation == "*":
            final_result += mul(nums)
        else:
            print("error: unknown operator: " , operation)
print(final_result)