result = 0
fresh_ids = []
file = open("../inputs/5.txt")


def sorting_func(id_range):
    # print("id: " + str(id_range[0]))
    return id_range[0]


for line in file:
    if line == "\n":
        break
    else:
        # print(line)
        id_range = line.strip()
        ids = id_range.split("-")
        fresh_ids.append((int(ids[0]), int(ids[1])))

# print(fresh_ids)

fresh_ids.sort(key=sorting_func)
print("sorted fresh ids: ", fresh_ids)

"""
sorted = open("sorted.txt", "w")
for fresh_id in fresh_ids:
    sorted.write(str(fresh_id) + "\n")
"""

merged_ids = [fresh_ids[0]]

for i in range(1, len(fresh_ids)):
    previous = merged_ids[len(merged_ids) - 1]
    current = fresh_ids[i]
    if current[0] > previous[1]:
        merged_ids.append(current)
        print("added")
    elif previous[1] < current[1]:
        merged_ids[len(merged_ids) - 1] = (previous[0], current[1])
        print("replaced")
    else:
        print("ignored")
    print("merged ids: ", merged_ids)

for merged_id in merged_ids:
    result += merged_id[1] - merged_id[0] + 1

print(result)
