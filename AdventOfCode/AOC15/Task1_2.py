with open("Task_Day1.txt","r") as infile:
    lines = infile.readlines()

line = lines[0]
acc = 0
for i in range(len(line)):
    if line[i] == "(":
        acc += 1
    elif line[i] == ")":
        acc -= 1
    if acc == -1:
        print(i+1)
        break