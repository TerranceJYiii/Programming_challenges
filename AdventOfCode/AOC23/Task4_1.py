with open("Task_Day4.txt","r") as infile:
    lines = infile.readlines()

points = 0
for line in lines:
    line = line.replace(":", "|")
    data = line.split("|")
    winning = data[1].strip().split()
    own = data[2].strip().split()
    num_of_win = 0
    for each in winning:
        if each in own:
            num_of_win += 1
    if num_of_win:
        points += (2**(num_of_win-1))

print(points)