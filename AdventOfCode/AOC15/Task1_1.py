with open("Task_Day1.txt","r") as infile:
    lines = infile.readlines()

line = lines[0]
a = line.count("(")
b = line.count(")")
print(a,b,a-b)