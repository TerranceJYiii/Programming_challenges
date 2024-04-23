with open("Task_Day3.txt","r") as infile:
    lines = infile.readlines()
line = lines[0]

x,y = 0,0
delivered = [(0,0)]
da = delivered.append
for i in range(len(line)):
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