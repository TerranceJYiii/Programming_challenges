print("""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?\n""")
from math import sqrt

def getsum(n):
    return sum(range(1,n+1))

def getdivisors(n):
    middle = int(sqrt(n))+1
    i = 1
    divisorlist = []
    for i in range(1,middle):
        if n%i ==0:
            divisorlist.append(i)
            divisorlist.append(n//i)

    # print(divisorlist)
    return(len(divisorlist))

# number = int(input('\nPlease provide the input\n'))
# tri = getsum(number)
# numofdivisor = getdivisors(tri)
# print (tri)
# print(numofdivisor)

i = 8
answer = getdivisors(getsum(i))
while answer<500:
    i += 1
    answer = getdivisors(getsum(i))
print(i)
print(getsum(i))