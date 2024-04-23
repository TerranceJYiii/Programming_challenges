import numpy as np
with open("Task_Day6.txt","r") as infile:
    lines = infile.readlines()

a = np.zeros((1000,1000))
for line in lines:
    instruction = line.split()
    
    if instruction[0] == "turn":
        x1,y1 = map(int,instruction[2].split(","))
        x2,y2 = map(int,instruction[-1].split(","))
        if instruction[1] == "on":
            for x in range(x1,x2+1):
                a[x,y1:y2+1] = 1
        else:
            for x in range(x1,x2+1):
                a[x,y1:y2+1] = 0
    else:
        x1,y1 = map(int,instruction[1].split(","))
        x2,y2 = map(int,instruction[-1].split(","))
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                a[x,y] = not(a[x,y]) 

print(np.count_nonzero(a))