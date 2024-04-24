print("""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.""")

from math import sqrt

truncprime = []

def isPrime(n): # Finds whether n is prime or not.
    if n == 1: return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def checkRTL(n):
    prime = True
    while n > 9:
        n = n // 10
        # print(n)
        if isPrime(n):
            continue
        else:
            prime = False
            break
    return prime

def checkLTR(n):
    prime = True
    while n > 9:
        temp = list(str(n))
        temp.remove(temp[0])
        num = "".join(temp)
        n = int(num)
        # print(n)
        if isPrime(n):
            continue
        else:
            prime = False
            break
    return prime


for i in range(13,1000000,2):
    if isPrime(i):
        if checkRTL(i):
            if checkLTR(i):
                truncprime.append(i)

print(truncprime)
print(sum(truncprime))