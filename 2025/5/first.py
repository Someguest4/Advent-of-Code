result = 0
product_ids = []
fresh_ids = []
file = open("../inputs/5.txt")

for line in file:
    if line == "\n":
        product_ids = file.readlines()
        break
    else:
        print(line)
        id_range = line.strip()
        ids = id_range.split("-")
        fresh_ids.append((int(ids[0]),int(ids[1])))

print(product_ids)
print(fresh_ids)

for product_id in product_ids:
    for fresh_id in fresh_ids:
        if fresh_id[0] <= int(product_id.strip()) <= fresh_id[1]:
            result += 1
            break

print(result)
