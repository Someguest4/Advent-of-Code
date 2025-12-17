import re

toggle = {
    "#": ".",
    ".": "#"
}

def find_best(buttons, end_state, queue):
    visited_states = set()
    while queue:
        current_state, steps = queue.pop(0)
        print(steps)
        if current_state == end_state:
            return steps

        for button in buttons:
            temp_current_state = [char for char in current_state]
            #print("temp_current state : ", temp_current_state, "for button ", button)
            for wire in button:
                temp_current_state[wire] = toggle[temp_current_state[wire]]
            #print("changed temp_current state : ", temp_current_state, "for button ", button)
            temp_current_state_str = "".join(temp_current_state)
            if temp_current_state_str not in visited_states:
                queue.append((temp_current_state_str, steps + 1))
                visited_states.add(temp_current_state_str)
            #print(button)


file = open("../inputs/10.txt")
result = 0

for i, line in enumerate(file):
    print("\n", "line ", i, " start")
    find = re.match("\[(.*)] (.*) {(.*)}\n?", line)
    line = find.groups()

    end_state = line[0]
    #print("end_state: ", end_state)
    #print("line: ", line)

    buttons = line[1]
    buttons = re.findall("\(([^)]*)\)", buttons)
    buttons = [set(map(int, line.split(","))) for line in buttons]
    #print("buttons: ", buttons)

    current_state = "." * len(end_state)
    #print("current state: ", current_state)
    queue = [(current_state, 0)]
    result += find_best(buttons, end_state, queue)

print(result)
