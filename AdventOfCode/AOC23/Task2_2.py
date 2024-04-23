with open("Task_Day2.txt","r") as infile:
    lines = infile.readlines()

power = 0
for line in lines:
    r,g,b = 0,0,0
    line = line.replace(":", ",").replace(";", ",")
    ls = list(map(lambda e: e.split(), line.rsplit(", ")))
    l = len(ls)
    for i in range(1,l):
        num = int(ls[i][0])
        color = ls[i][1]
        if color == "red":
            r = max(r,num)
        elif color == "green":
            g = max(g,num)
        elif color == "blue":
            b = max(b,num)
    game_power = r*g*b
    power += game_power
    # print(game_power)

print(power)