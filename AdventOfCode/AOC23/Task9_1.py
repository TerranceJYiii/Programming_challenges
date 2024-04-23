with open("Task_Day9.txt","r") as infile:
    lines = infile.readlines()

ans = []
for line in lines:
    sequence = [list(map(int,line.split()))]
    while any(sequence[-1]):
        temp = []
        ta = temp.append
        for i in range(len(sequence[-1])-1):
            ta(sequence[-1][i+1]-sequence[-1][i])
        sequence.append(temp)
    for i in range(len(sequence)-2,-1,-1):
        sequence[i].append(sequence[i][-1] + sequence[i+1][-1])
    ans.append(sequence[0][-1])

print(ans)
print(sum(ans))