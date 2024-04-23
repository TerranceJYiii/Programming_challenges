with open("Task_Day3.txt","r") as infile:
    lines = infile.readlines()
line = lines[0]

delivered = [(0,0)]
da = delivered.append

for a in [0,1]:
    x,y = 0,0
    for i in range(a,len(line),2):
    # for each in line:
        each = line[i]
        if each == "^":
            y += 1
        elif each == "v":
            y -= 1
        elif each == ">":
            x += 1
        elif each == "<":
            x -= 1
        # print((x,y))
        da((x,y))

# print(delivered)
s = set(delivered)
# print(s)
print(len(s))