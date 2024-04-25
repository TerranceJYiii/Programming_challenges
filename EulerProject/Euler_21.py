from math import sqrt

print("""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000. """)


def getamicable(n):
    middle = int(sqrt(n))+1
    i = 1
    divisorlist = []
    for i in range(1,middle):
        if n%i ==0:
            divisorlist.append(i)
            divisorlist.append(n//i)

    sort = sorted(divisorlist)
    sort.pop()
    amicable = sum(sort)
    return(amicable)

n = int(input("\nPlease provide the input \n"))
# print(getamicable(n))

amicablelist = []
ap = amicablelist.append
for i in range(1, n+1):
    if i not in amicablelist:
        amicablepair = getamicable(i)
        # print(i, "==>", amicablepair)
        if i == getamicable(amicablepair) and i != amicablepair:
            ap(i)
            ap(getamicable(i))

print(amicablelist)
print(sum(amicablelist))
