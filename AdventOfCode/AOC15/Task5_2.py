with open("Task_Day5.txt","r") as infile:
    lines = infile.readlines()

ans = 0
for line in lines:
    cond1 = False
    for i in range(len(line)-1):
        if line.count(line[i:i+2])> 1:
            cond1 = True
            break
    if cond1:
        for j in range(len(line)-2):
            if line[j] == line[j+2]:
                ans += 1
                break
    
print(ans)