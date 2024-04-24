print("""It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square? """)

from math import sqrt

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

primelist = []
pa = primelist.append
doublesquare = []
da = doublesquare.append

for i in range(2, 100000):
    if isPrime(i):
        pa(i)

for i in range(1,1000):
    da(2*(i**2))
# print(doublesquare)

value = 35
notSolved = True
while notSolved : 
    if value not in primelist:
        found = False
        for prime in primelist:
            if value > prime:
                temp = value - prime
                if temp not in doublesquare:
                    continue
                else:
                    found = True 
                    print(value, prime, temp)
                    break
            else: break
        if found:
            value += 2
            continue
        else:
            print(value, "is the answer")
            notSolved = False
    else:
        print(value, "is Prime")
        value += 2
