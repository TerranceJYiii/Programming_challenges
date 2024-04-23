with open("Task_Day10.txt","r") as infile:
    lines = infile.readlines()

#up = 0, left = 1, right = 2, down = 3
def check_direction(now_row,now_column,direction):
    this_way = True
    next_direction = None
    if direction == 0:
        next = lines[now_row - 1][now_column]
        if next == "|":
            next_direction = 0
        elif next == "7":
            next_direction = 1
        elif next == "F":
            next_direction = 2
        else:
            this_way = False
    elif direction == 1:
        next = lines[now_row][now_column-1]
        if next == "-":
            next_direction = 1
        elif next == "L":
            next_direction = 0
        elif next == "F":
            next_direction = 3
        else:
            this_way = False
    elif direction == 2:
        next = lines[now_row][now_column+1]
        if next == "-":
            next_direction = 2
        elif next == "J":
            next_direction = 0
        elif next == "7":
            next_direction = 3
        else:
            this_way = False
    elif direction == 3:
        next = lines[now_row+1][now_column]
        if next == "|":
            next_direction = 3
        elif next == "L":
            next_direction = 2
        elif next == "J":
            next_direction = 1
        else:
            this_way = False

    return this_way, next_direction

for i in range(len(lines)):
    if "S" in lines[i]:
        row, column = i, lines[i].index("S")
        break

print(row,column)

#up = 0, left = 1, right = 2, down = 3
route = []
for i in range(4):
    this_way,next_direction = check_direction(row, column, i)
    if this_way:
        if i == 0:
            route.append([row-1,column,next_direction,1])
        elif i == 1:
            route.append([row,column-1,next_direction,1])
        elif i == 2:
            route.append([row,column+1,next_direction,1])
        elif i == 3:
            route.append([row+1,column,next_direction,1])

print(route)

complete = False
while not complete:
    for each in [0,1]:
        r,c,n,v = route[each]
        this_way,next_direction = check_direction(r,c,n)
        if this_way:
            if n == 0:
                route[each] = [r-1,c,next_direction,v+1]
            elif n == 1:
                route[each] = [r,c-1,next_direction,v+1]
            elif n == 2:
                route[each] = [r,c+1,next_direction,v+1]
            elif n == 3:
                route[each] = [r+1,c,next_direction,v+1]
    print(route)
    if route[0][:2] == route[1][:2]:
        complete = True

print(route)
print(route[0][3])