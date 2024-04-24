print("""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?""")

from math import sqrt

def findPrimeFactor(n):
    pflist = []
    while n > 1:
        for i in primelist:
            if n % i == 0:
                n /= i
                if i not in pflist:
                    pflist.append(i)
                break
    # print(pflist)
    return len(pflist)



def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

primelist = [2]
pa = primelist.append

for i in range(3, 00000, 2):
    if isPrime(i):
        pa(i)

# print(primelist)

for index in range(len(primelist)-1):
    now = primelist[index]
    next = primelist[index + 1]
    if (next - now) > 4:
        start = now + 1
        success = 0
        for i in range(now+1, next):
            # print(i)
            if findPrimeFactor(i) != 4:
                success = 0
                start = i + 1
                continue
            else:
                success += 1
                if success == 4:
                    print("success",now, next, start)

