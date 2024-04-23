with open("Task_Day2.txt","r") as infile:
    lines = infile.readlines()

ans = 0
for line in lines:
    a,b,c = map(int,line.split("x"))
    d,e,f = a*b, b*c, a*c
    ans += 2*(d+e+f)+min(d,e,f)

print(ans)