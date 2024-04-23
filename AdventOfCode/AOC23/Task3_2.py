with open("Task_Day3.txt","r") as infile:
    lines = infile.readlines()

array = []
for line in lines:
    array.append(line[:-1])

row = len(array)
column = len(array[0])

def determine_middle(r,c):
    num = array[r][c]
    try:
        if array[r][c-1].isdigit():
            num = array[r][c-1] + num
            if array[r][c-2].isdigit():
                num = array[r][c-2] + num
    except IndexError:
        pass
    try:
        if array[r][c+1].isdigit():
            num += array[r][c+1]
            if array[r][c+2].isdigit():
                num += array[r][c+2]
    except IndexError:
        pass
    return int(num)
    
def determine_left(r,c):
    num = array[r][c]
    try:
        if array[r][c-1].isdigit():
            num = array[r][c-1] + num
            if array[r][c-2].isdigit():
                num = array[r][c-2] + num
    except IndexError:
        pass
    return int(num)

def determine_right(r,c):
    num = array[r][c]
    try:
        if array[r][c+1].isdigit():
            num += array[r][c+1]
            if array[r][c+2].isdigit():
                num += array[r][c+2]
    except IndexError:
        pass
    return int(num)

def check_gear(r,c):
    num = []
    if r > 0:
        if array[r-1][c].isdigit():
            num.append(determine_middle(r-1,c))
        else:
            if c > 0:
                if array[r-1][c-1].isdigit():
                    num.append(determine_left(r-1,c-1))
            if c < column - 1:
                if array[r-1][c+1].isdigit():
                    num.append(determine_right(r-1,c+1))
    if c > 0:
        if array[r][c-1].isdigit():
            num.append(determine_left(r,c-1))
    if c < column - 1:
        if array[r][c+1].isdigit():
            num.append(determine_right(r,c+1))
    if r < row-1:
        if array[r+1][c].isdigit():
            num.append(determine_middle(r+1,c))
        else:
            if c > 0:
                if array[r+1][c-1].isdigit():
                    num.append(determine_left(r+1,c-1))
            if c < column - 1:
                if array[r+1][c+1].isdigit():
                    num.append(determine_right(r+1,c+1))
    
    if len(num) == 2:
        print(num)
        return num[0] * num[1]
    return 0

gear = 0
for r in range(row):
    if "*" not in array[r]:
        continue
    for c in range(column):
        if array[r][c] != "*":
            continue
        else:
            gear += check_gear(r,c)

print(gear)