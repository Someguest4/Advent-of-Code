file = open("../inputs/9.txt")
tiles = []
for line in file:
    tiles.append(tuple(map(int, file.readline().strip().split(","))))


def find_area(x1, y1, x2, y2):
    x_dist = abs(x1 - x2) + 1
    y_dist = abs(y1 - y2) + 1
    area = x_dist * y_dist
    return area


rectangles = []
for i in range(len(tiles)):
    first_tile = tiles[i]
    for j in range(i + 1, len(tiles)):
        second_tile = tiles[j]
        rectangles.append(find_area(first_tile[0], first_tile[1], second_tile[0], second_tile[1]))

result = max(rectangles)
print(result)
