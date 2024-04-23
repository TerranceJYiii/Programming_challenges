with open("Task_Day2.txt","r") as infile:
    lines = infile.readlines()

ans = 0
for line in lines:
    a,b,c = map(int,line.split("x"))
    mx = max(a,b,c)
    ans += a*b*c + 2*(a+b+c-mx)

print(ans)