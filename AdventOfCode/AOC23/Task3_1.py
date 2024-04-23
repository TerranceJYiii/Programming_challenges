with open("Task_Day3.txt","r") as infile:
    lines = infile.readlines()

array = []
for line in lines:
    array.append(line[:-1])

row = len(array)
column = len(array[0])

def check_part(r,c,num_len):
    if r > 0:
        if c > 0:
            char = array[r-1][c-1]
            if char != "." and not char.isdigit():
                return True
        for i in range(c,c+num_len):
            char = array[r-1][i]
            if char != "." and not char.isdigit():
                return True
        if c+num_len < column-1:
            char = array[r-1][c+num_len]
            if char != "." and not char.isdigit():
                return True
    if c > 0:
        char = array[r][c-1]
        if char != "." and not char.isdigit():
            return True
    if c+num_len < column-1:
        char = array[r][c+num_len]
        if char != "." and not char.isdigit():
            return True
    if r < row-1:
        if c > 0:
            char = array[r+1][c-1]
            if char != "." and not char.isdigit():
                return True
        for i in range(c,c+num_len):
            char = array[r+1][i]
            if char != "." and not char.isdigit():
                return True
        if c+num_len < column-1:
            char = array[r+1][c+num_len]
            if char != "." and not char.isdigit():
                return True
    return False

ans = 0
skip = 0
for r in range(row):
    for c in range(column):
        if skip > 0:
            skip -= 1
            continue
        num_len = 0
        try:
            if array[r][c].isdigit():
                num_len = 1
                if array[r][c+1].isdigit():
                    num_len = 2
                    skip = 1
                    if array[r][c+2].isdigit():
                        num_len = 3
                        skip = 2
        except IndexError:
            pass
        if num_len > 0:
            if check_part(r,c,num_len):
                temp = array[r][c:c+num_len]
                ans += int(temp)

print(ans)