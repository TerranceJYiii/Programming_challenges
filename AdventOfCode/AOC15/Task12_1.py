with open("Task_Day12.txt","r") as infile:
    lines = infile.readlines()

ans = 0
temp = ""
line = lines[0]
for each in line:
    if each.isdigit() or each == "-":
        temp += each
    else:
        if temp == "":
            continue
        else:
            ans += int(temp)
            temp = ""
print(ans)