print("""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.""")

from math import factorial

factorials = {"0":factorial(0), "1":factorial(1), "2":factorial(2), "3":factorial(3), "4":factorial(4), "5":factorial(5), "6":factorial(6), "7":factorial(7), "8":factorial(8), "9":factorial(9)}

anslist = []

def checkfac(i):
    temp = 0
    stri = str(i)
    for each in stri:
        temp += factorials.get(each)
        if temp > i:
            return False
    if temp == i:
        return True
    else:
        return False

for i in range(10,2000000):
    if checkfac(i):
        anslist.append(i)

print(anslist)
print(sum(anslist))