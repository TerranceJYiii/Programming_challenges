print("""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes? """)

from math import sqrt

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

primelist = [2]
pa = primelist.append
for i in range(3,5000,2):
    if isPrime(i):
        pa(i)
primetuple = tuple(primelist)

max = 0
temp = 0
cnt = 0

for i in primetuple:
    temp += i 
    cnt += 1
    print(temp,i)
    if temp < 1000000:
        max = temp
        if isPrime(temp): 
            print(max,"is prime with", cnt, "term")
    elif temp >= 1000000:
        break
print(max)

for i in primetuple:
    temp = max - i
    if isPrime(temp):
        print(temp,"is answer")
        break
    else:
        max = temp


# extracount = 0
# temp = max
# while max < 1000000:
#     max = max + primetuple[536+extracount] - primetuple[extracount]
#     print(max)
#     extracount += 1
#     if isPrime(max):
#         temp = max
#         print(max,"is Prime")
# print(temp)

