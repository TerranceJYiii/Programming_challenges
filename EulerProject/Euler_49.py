print("""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence? """)

from itertools import permutations
from math import sqrt

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def checkap(numlist):
    anslist = []
    for i in range(len(numlist)-1):
        a = numlist[i]
        for j in range(i+1, len(numlist)):
            b = numlist[j]
            anslist.append((a,b,a-b))
    # print(anslist)
    for i in range(len(anslist)-1):
        if anslist[i][2] == 0:
            continue
        for j in range(i+1, len(anslist)):
            if anslist[j][2] == 0:
                continue
            if anslist[i][1] == anslist[j][0]:
                if anslist[i][2] == anslist[j][2]:
                    print(anslist[i][0], anslist[i][1], anslist[j][1], anslist[j][2])



        

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for a in range(10):
    num1 = num[a]
    for b in range(10):
        num2 = num[b]
        for c in range(10):
            num3 = num[c]
            for d in range(10):
                num4 = num[d]
                combination = num1 + num2 + num3 + num4
                
                numlist = []
                for each in permutations(combination):
                    n = (int("".join(each)))
                    if not isPrime(n) or n < 1000:
                        continue
                    else:
                        numlist.append(n)
                # print(combination, numlist)
                if len(numlist) >= 3:
                    numlist.sort(reverse=True)
                    checkap(numlist)


# numlist = []
# for each in permutations("1478"):
#     n = (int("".join(each)))
#     if not isPrime(n):
#         continue
#     else:
#         numlist.append(n)
                
# print(numlist)
# if len(numlist) >= 3:
#     numlist.sort(reverse=True)
#     checkap(numlist)