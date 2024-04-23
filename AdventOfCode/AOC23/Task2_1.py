#12 red cubes, 13 green cubes, and 14 blue cubes

with open("Task_Day2.txt","r") as infile:
    lines = infile.readlines()

ans = 0
for line in lines:
    possible = True
    line = line.replace(":", ",").replace(";", ",")
    ls = list(map(lambda e: e.split(), line.rsplit(", ")))
    l = len(ls)
    for i in range(1,l):
        num = int(ls[i][0])
        color = ls[i][1] 
        if num <= 12:
            continue
        elif num > 12 and color == "red":
            possible = False
            break
        elif num > 13 and color == "green":
            possible = False
            break
        elif num > 14 and color == "blue":
            possible = False
            break
        else:
            continue
    if possible:
        ans += int(ls[0][1])

print(ans)