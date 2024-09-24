with open("Task_Day6.txt","r") as infile:
    lines = infile.readlines()

alphabet = "qwertyuiopasdfghjklzxcvbnm"

def Task1():
    ans = ""
    for i in range(8):
        letter = "".join([line[i] for line in lines])
        maxima = 0
        for each in alphabet:
            x = letter.count(each)
            if x > maxima:
                maxima = x
                temp = each
        ans += temp
    return ans

def Task2():
    ans = ""
    for i in range(8):
        letter = "".join([line[i] for line in lines])
        minima = 2048
        for each in alphabet:
            x = letter.count(each)
            if x < minima:
                minima = x
                temp = each
        ans += temp
    return ans

ans = Task2()
print(ans)