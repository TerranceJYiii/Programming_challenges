print("""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.""")

from math import sqrt

def getpds(n): #pds = proper divisor sum
    middle = int(sqrt(n))+1
    divisorlist = []
    for i in range(1,middle):
        if n%i ==0:
            divisorlist.append(i)
            if n//i != i:
                divisorlist.append(n//i)


    sort = sorted(divisorlist)
    sort.pop()
    pds = sum(sort)
    # print(n, "==>", pds)
    return (pds > n)

n = int(input("\nPlease provide the input \n"))
# print(getpds(n))
abundantlist = []
ap = abundantlist.append
for i in range(1, n+1):
    if (getpds(i)):
        ap(i)

print(abundantlist)

cannotlist = []
cp = cannotlist.append
length = len(abundantlist)
for i in range(n+1):
    print(i)
    for j in range(length+1):
        if j == length:
            cp(i)
            break
        if abundantlist[j] > i:
            cp(i)
            break
        else:
            temp = i - abundantlist[j]
            if temp in abundantlist:
                break
            else:
                continue
        
print(cannotlist)
print(sum(cannotlist))



