print("""Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1? """)


def checkPandig(ans):
    if "0" in ans:
        return False
    else:
        for each in ans:
            if ans.count(each) > 1:
                return False
    return True

maxima = 0

for n in range(2,100000):
    ans = ""
    for j in range(1,9):
        ans += str(n*j)
        l = len(ans)
        if l<9:
            continue
        elif l>9:
            break
        else:
            if checkPandig(ans):
                maxima = max(maxima, int(ans))


print(maxima)