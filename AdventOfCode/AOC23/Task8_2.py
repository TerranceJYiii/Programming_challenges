from math import lcm

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
nows = []
ends = []
for line in lines[2:]:
    source,des1,des2 = formatting_line(line)
    maps[source] = [des1,des2]
    if source[-1] == "A":
        nows.append(source)
    if source[-1] == "Z":
        ends.append(source)
print(nows, ends)

l = len(steps)

tracks = []
for each in nows:    
    current_step = 0
    walked = 0
    while each[-1]!= "Z":
        if current_step == l-1:
            current_step -= l-1
        if steps[current_step] == "L":
            each = maps[each][0]
            walked += 1
            current_step += 1
        elif steps[current_step] == "R":
            each = maps[each][1]
            walked += 1
            current_step += 1
    tracks.append(walked)

a,b,c,d,e,f = tracks
print(tracks)
print(lcm(a,b,c,d,e,f))


