print("""Project Euler 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?""")

### HACKERRANK MY SOLUTION
# import sys

# def detect_factors(n):
#     factors = []
#     append = factors.append
#     for i in range(1, n+1):
#         if n%i == 0:
#             append(i)
#     return factors

# def detect_prime_numbers(factors):
#     primefactors = []
#     for f in factors:
#         if f > 1:
#             for each in range(3,f):
#                 if f % each ==0:
#                     break
#             else:
#                 primefactors.append(f)
#     return primefactors
    
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     factors = detect_factors(n)
#     primefactors = detect_prime_numbers(factors)
#     print(max(primefactors))        
    

from math import sqrt

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def maxPrimeFactor(n):
    max = 1
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            if isPrime(n//i) and n//i > max:
                max = n//i
                break
            elif isPrime(i): max = i        
    return max
    
print(maxPrimeFactor(int(input("\nPlease provide the input \n"))))