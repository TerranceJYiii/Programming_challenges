with open("Task_Day1.txt","r") as infile:
    lines = infile.readlines()

sum = 0
for each in lines:
    temp = ""
    for c in each:
        if c.isdigit():
            temp = c
            break
    for invc in each[::-1]:
        if invc.isdigit():
            temp += invc
            break
    # print(temp)
    sum += int(temp)
    
print(sum)