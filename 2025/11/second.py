from linecache import cache

file = open("../inputs/11.txt")

in_out_map = {

}
for line in file:
    line = line.strip().split(":")
    outputs = line[1].strip().split()
    in_out_map[line[0]] = outputs




# print(in_out_map)
def dfs(current, end):
    if current in cache:
        return cache[current]
    # print("current: " , current)

    result = 0
    if current == end:
        result = 1
    elif current == "out":
        result = 0
    else:
        for child in in_out_map[current]:
            result += dfs(child, end)

    cache[current] = result
    return result

cache = {

}

svr_to_fft = dfs("svr", "fft")
cache.clear()
svr_to_dac = dfs("svr", "dac")
cache.clear()
fft_to_dac = dfs("fft", "dac")
cache.clear()
dac_to_fft = dfs("dac", "fft")
cache.clear()
fft_to_out = dfs("fft", "out")
cache.clear()
dac_to_out = dfs("dac", "out")


print("svr-fft", svr_to_fft)
print("svr-dac", svr_to_dac)
print("fft-dac", fft_to_dac)
print("dac-fft", dac_to_fft)
print("fft-out", fft_to_out)
print("dac-out", dac_to_out)

svr_fft_dac_out = svr_to_fft * fft_to_dac * dac_to_out
svr_dac_fft_out = svr_to_dac * dac_to_fft * fft_to_out

result = svr_fft_dac_out + svr_dac_fft_out
print("result: " , result)