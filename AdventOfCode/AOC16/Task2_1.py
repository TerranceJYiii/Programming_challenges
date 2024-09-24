with open("Task_Day2.txt","r") as infile:
    lines = infile.readlines()

# x0 = row (UD), y1 = col (LR)
numpad = [[1,2,3],[4,5,6],[7,8,9]]
def move(direction,val):
    direction += val
    if direction < 0:
        direction = 0
    elif direction > 2:
        direction = 2
    return direction
i = 0
x,y = 1,1
for line in lines:
    for each in line:
        if each == "U":
            x = move(x,-1)
        elif each == "D":
            x = move(x,1)
        elif each == "L":
            y = move(y,-1)
        elif each == "R":
            y = move(y,1)
    i += 1
    print(numpad[x][y], i)
          