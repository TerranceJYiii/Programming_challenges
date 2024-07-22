with open("Task_Day23.txt","r") as infile:
    lines = infile.readlines()


l = len(lines)
for i in range(l):
    lines[i] = lines[i].split()

a = 1   # Task23_1, a = 0; Task23_2, a = 1;
b = 0   
i = 0
while i < l:
    if lines[i][0] == "inc":
        if lines[i][1] == "a":
            a += 1
        else:
            b += 1
        i += 1

    elif lines[i][0] == "hlf":
        if lines[i][1] == "a":
            a /= 2
        else:
            b /= 2
        i += 1
    
    elif lines[i][0] == "tpl":
        if lines[i][1] == "a":
            a *= 3
        else:
            b *= 3
        i += 1
    
    elif lines[i][0] == "jmp":
        i += int(lines[i][1])

    elif lines[i][0] == "jio":
        if a == 1:
            i += int(lines[i][2])
        else:
            i += 1
    
    elif lines[i][0] == "jie":
        if a % 2 == 0:
            i += int(lines[i][2])
        else:
            i += 1
    
    # print(a,b,i)

print(a,b,i)