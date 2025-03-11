with open("Task_Day9.txt","r") as infile:
    lines = infile.readlines()

line = lines[0]
l = len(line)

def Task9_2(i, l):
    ans = 0
    while i < l:
        if line[i] != "(":
            ans += 1
            i += 1
        else:
            for j in range(1,10):
                if line[i+j] == ")":
                    num_of_char, repeat = map(int,line[i+1:i+j].split("x"))
                    ans += Task9_2(i + j + 1,num_of_char + i + j + 1) * repeat
                    i += j + num_of_char + 1
                    break
    return ans

ans = Task9_2(0,l)
print(ans)

