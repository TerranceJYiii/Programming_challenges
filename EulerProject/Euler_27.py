print("""Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0<n<39
. However, when n = 40, answer is divisible by 41, and certainly when n = 41, answer is clearly divisible by 41.

The incredible formula 
n^2 - 79n + 1601
was discovered, which produces 80 primes for the consecutive values 0<n<79
. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000 
where |n| is the modulus/absolute value of n 

Find the product of the coefficients, 
a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0. """)

from math import sqrt

prime_numbers = [-997, -991, -983, -977, -971, -967, -953, -947, -941, -937, -929, -919, -911, -907, -887, -883, -881, -877, -863, -859, -857, -853, -839, -829, -827, -823, -821, -811, -809, -797, -787, -773, -769, -761, -757, -751, -743, -739, -733, -727, -719, -709, -701, -691, -683, -677, -673, -661, -659, -653, -647, -643, -641, -631, -619, -617, -613, -607, -601, -599, -593, -587, -577, -571, -569, -563, -557, -547, -541, -523, -521, -509, -503, -499, -491, -487, -479, -467, -463, -461, -457, -449, -443, -439, -433, -431, -421, -419, -409, -401, -397, -389, -383, -379, -373, -367, -359, -353, -349, -347, -337, -331, -317, -313, -311, -307, -293, -283, -281, -277, -271, -269, -263, -257, -251, -241, -239, -233, -229, -227, -223, -211, -199, -197, -193, -191, -181, -179, -173, -167, -163, -157, -151, -149, -139, -137, -131, -127, -113, -109, -107, -103, -101, -97, -89, -83, -79, -73, -71, -67, -61, -59, -53, -47, -43, -41, -37, -31, -29, -23, -19, -17, -13, -11, -7, -5, -3, -2, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 
373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 
997]

def isPrime(n): # Finds whether n is prime or not.
    if n in prime_numbers:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: 
            return False
    return True

maxnum = 0
maxa = 0
maxb = 0

for a in range(-999,999):
    for b in prime_numbers:
        for n in range(0,1000):
            temp = n**2 + a*n + b
            if temp > 0:
                if isPrime(temp):
                    continue
                else:
                    if n <= 1:
                        break
                    else:
                        print("a =", a," b =", b, " n =", n)
                        if maxnum < n:
                            maxnum = n
                            maxa = a
                            maxb = b
                        break
            else:
                print("a =", a," b =", b, " n =", n)
                break
                
print(maxnum)
print(maxa, maxb)
