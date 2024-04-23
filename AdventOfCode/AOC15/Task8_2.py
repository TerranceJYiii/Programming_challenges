with open("Task_Day8.txt","r") as infile:
    lines = infile.readlines()
# print(len(lines))
ans = 0
for line in lines:
    temp_ans = 2 + line.count("\\") + line.count("\"")
    ans += temp_ans
print(ans)