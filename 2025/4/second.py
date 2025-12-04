result = 0
file = open("../inputs/4.txt")


def print_array(array):
    for item in array:
        print(item)


def create_array_from_file(file_for_array):
    array = []
    for line in file_for_array:
        row = []
        line = line.strip()
        for char in line:
            row.append(char)
        array.append(row)
    return array


def check_neighbours(grid, x, y, symbol):
    symbol_count = 0
    neighbours = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                  (x + 1, y + 1)]
    for neighbour in neighbours:
        if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]):
            if grid[neighbour[0]][neighbour[1]] == symbol:
                symbol_count += 1
    return symbol_count


grid = create_array_from_file(file)
print_array(grid)
temp = 1
while temp != 0:
    temp = 0
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == "@":
                if check_neighbours(grid, x, y, "@") < 4:
                    grid[x][y] = "."
                    result += 1
                    temp += 1
    print_array(grid)
print(result)
