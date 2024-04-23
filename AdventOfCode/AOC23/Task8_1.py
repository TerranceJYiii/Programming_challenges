with open("Task_Day8.txt","r") as infile:
    lines = infile.readlines()

def formatting_line(line):
    line = line.replace("(", " ")
    line = line.replace(",", " ")
    line = line.replace(")", " ")
    line = line.replace("=", " ")
    a,b,c = line.split()
    return a,b,c

steps = lines[0]

maps = {}
for line in lines[2:]:
    source,des1,des2 = formatting_line(line)
    maps[source] = [des1,des2]

l = len(steps)
current_step = 0
now = "AAA"
walked = 0

while now != "ZZZ":
    print(now)
    if current_step == l-1:
        current_step -= l-1
    if steps[current_step] == "L":
        now = maps[now][0]
        walked += 1
        current_step += 1
    elif steps[current_step] == "R":
        now = maps[now][1]
        walked += 1
        current_step += 1
print(walked)


