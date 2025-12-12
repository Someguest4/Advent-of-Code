final_result = 0
grid = []
file = open("../inputs/6.txt")
lines = file.readlines()


def print_grid(grid):
    for row in grid:
        print(row)


for line in lines:
    dirty_row = line
    # print(dirty_row)
    row = []
    for i, char in enumerate(dirty_row):
        if char != "\n":
            row.append(char)
    grid.append(row)

print_grid(grid)
temp_result = 0
for column_id in range(len(grid[0])):

    num = ""

    # print("l", len(grid[0]))
    last_row = grid[len(grid) - 1]
    if column_id < len(last_row):
        new_operation = grid[len(grid) - 1][column_id]
        if new_operation.strip() != "":
            final_result += temp_result
            operation = new_operation
            if operation == "*":
                temp_result = 1
            else:
                temp_result = 0
    for row_id in range(len(grid) - 1):
        num += grid[row_id][column_id]

    if num.strip() == "":
        continue
    num = int(num)
    # print(num)

    # print(operation)
    if operation == "+":
        temp_result += num
    elif operation == "*":
        temp_result *= num
    else:
        print("error: unknown operator: ", operation)
final_result += temp_result
# print(final_result)
# print_grid(grid)
print(final_result)
