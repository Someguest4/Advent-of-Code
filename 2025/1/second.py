number = 50
result = 0
file = open("../inputs/1.txt")

actions = file.readlines()
for action in actions:
    action_num = int(action[1:])

    if action[0] == "L":
        result += abs((number - action_num) // 100)
        if abs(action_num - number) % 100 == 0:
            result += 1
        if number == 0:
            result -= 1

        number = (number - action_num) % 100

    else:
        result += (number + action_num) // 100
        number = (number + action_num) % 100

print(result)
