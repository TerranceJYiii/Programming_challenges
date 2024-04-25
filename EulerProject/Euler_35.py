print("""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?""")

from math import sqrt

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def checkCircular(i):
    isCirc = True
    lis = []
    temp = i
    l = len(str(i))
    bv = temp//(10**(l-1))
    for j in range(l):
        temp = temp*10 - (bv*(10**l)) + bv
        bv = temp//(10**(l-1))
        if temp in primelist:
            lis.append(temp)
        else:
            isCirc = False
            break
    if isCirc:
        return lis
    else:
        return[]
        

primelist = [2,3,5,7,11]
pa = primelist.append

circprime = []
cc = circprime.count
cr = circprime.remove


for i in range(13,1000000):
    if isPrime(i):
        pa(i)

# print(primelist)

for each in primelist:
    if each not in circprime:
        circprime += checkCircular(each)

# print(circprime)
circprime.sort()
for one in circprime:
    if cc(one)>1:
        for i in range(cc(one)-1):
            cr(one)

# print(circprime)
print(len(circprime))