with open("Task_Day9.txt","r") as infile:
    lines = infile.readlines()

line = lines[0]
l = len(line)
ans = 0
i = 0

while i < l:
    if line[i] != "(":
        ans += 1
        i += 1
    else:
        for j in range(1,15):
            if line[i+j] == ")":
                num_of_char,repeat = map(int,line[i+1:i+j].split("x"))
                ans += num_of_char*repeat
                i += j + num_of_char + 1
                break

print(ans)