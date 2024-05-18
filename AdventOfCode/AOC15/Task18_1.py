with open("Task_Day18.txt","r") as infile:
    lines = infile.readlines()

array = []
for line in lines:
    array.append(line[:-1])

row = len(array)
column = len(array[0])

# # Task 2: activale 2 line below
# array[0] = "#" + array[0][1:-1] + "#"
# array[-1] = "#" + array[-1][1:-1] + "#"

def check_part(r,c,current):
    on = 0
    if r > 0:
        if c > 0:
            char = array[r-1][c-1]
            if char == "#" :
                on += 1
            
        char = array[r-1][c]
        if char == "#" :
            on += 1
        
        if c < column-1:
            char = array[r-1][c+1]
            if char == "#" :
                on += 1

    if c > 0:
        char = array[r][c-1]
        if char == "#" :
            on += 1

    if c < column-1:
        char = array[r][c+1]
        if char == "#" :
            on += 1
    
    if r < row-1:
        if c > 0:
            char = array[r+1][c-1]
            if char == "#" :
                on += 1
        
        char = array[r+1][c]
        if char == "#" :
            on += 1
        
        if c < column-1:
            char = array[r+1][c+1]
            if char == "#" :
                on += 1
    
    if on > 3 or on < 2:
        return "."
    elif on == 3:
        return "#"
    elif on == 2 and current == "#":
        return "#"
    else:
        return "."


temp = [ [ None for y in range(column) ] for x in range(row) ]

for i in range(100):
    for r in range(row):
        for c in range(column):
            temp[r][c] = check_part(r,c,array[r][c])
    array = [ [ temp[r][c] for c in range(column) ] for r in range(row) ]
    
    # # Task 2: activale 4 line below
    # array[0][0] = "#"
    # array[row-1][0] = "#"
    # array[0][column-1] = "#"
    # array[row-1][column-1] = "#"

ans = 0
for r in range(row):
    ans += array[r].count("#")

print(ans)