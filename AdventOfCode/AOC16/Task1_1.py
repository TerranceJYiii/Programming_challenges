with open("Task_Day1.txt","r") as infile:
    lines = infile.readlines()

instruction = lines[0].split(", ")
facing_direction = 200   #0 = N, 1 = E, 2 = S, 3 = W
horizontal = 0
vertical = 0
for each in instruction:
    direction, step = each[0], int(each[1:])
    if direction == "L":
        facing_direction -= 1
    elif direction == "R":
        facing_direction += 1

    facing = facing_direction % 4
    if facing == 0:
        vertical += step
    elif facing == 1:
        horizontal += step
    elif facing == 2:
        vertical -= step
    elif facing == 3:
        horizontal -= step
    # print(direction, facing, step, horizontal, vertical)

print(horizontal, vertical)
ans = abs(horizontal) + abs(vertical)
print(ans)