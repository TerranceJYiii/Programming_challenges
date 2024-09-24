with open("Task_Day3.txt","r") as infile:
    lines = infile.readlines()

def check_triangle(sides):
    a,b,c = sides
    return a+b > c and b+c > a and c+a > b

def task3_1():
    ans = 0
    for line in lines:
        triangle = map(int,line.split())
        if check_triangle(triangle):
            ans += 1
    print(ans)

def task3_2():
    ans = 0
    num_of_set = len(lines)//3
    for z in range(num_of_set):
        t1 = []
        t2 = []
        t3 = []
        for i in range(3):
            a,b,c = map(int,lines[z*3+i].split())
            t1.append(a)
            t2.append(b)
            t3.append(c)
        for each in [t1,t2,t3]:
            if check_triangle(each):
                ans += 1

    print(ans)

task3_2()