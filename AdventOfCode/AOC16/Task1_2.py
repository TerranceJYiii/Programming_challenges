with open("Task_Day1.txt","r") as infile:
    lines = infile.readlines()

instruction = lines[0].split(", ")
facing_direction = 200   #0 = N, 1 = E, 2 = S, 3 = W, NS = y, EW = x

passed_ways = {0:[0]}           #x:[y]
current_coordinate = [0,0]      #[x,y]

def record(coordinate):
    x,y = coordinate
    if x not in passed_ways:
        passed_ways[x] = [y]
        return False
    
    elif y not in passed_ways[x]:
        passed_ways[x].append(y)
        return False
    
    else:
        return True

for each in instruction:
    direction, step = each[0], int(each[1:])
    if direction == "L":
        facing_direction -= 1
    elif direction == "R":
        facing_direction += 1

    facing = facing_direction % 4
    if facing == 0:
        for i in range(step):
            current_coordinate[1] += 1
            done = record(current_coordinate)
            if done:
                break
    
    elif facing == 1:
        for i in range(step):
            current_coordinate[0] -= 1
            done = record(current_coordinate)
            if done:
                break
    
    elif facing == 2:
        for i in range(step):
            current_coordinate[1] -= 1
            done = record(current_coordinate)
            if done:
                break
    
    elif facing == 3:
        for i in range(step):
            current_coordinate[0] += 1
            done = record(current_coordinate)
            if done:
                break

    if done:
        print(current_coordinate)
        break

ansx,ansy = current_coordinate
print(current_coordinate)
print(abs(ansx) + abs(ansy))
