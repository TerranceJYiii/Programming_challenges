print(""""Project Euler 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
""")

n = int(input('\nPlease provide the input\n'))
prime_numbers = [2]
append = prime_numbers.append
for num in range(3,n+1,2):
    for i in prime_numbers:
        if num % i == 0:
            break
        if i == prime_numbers[-1]:
            append(num)

print(prime_numbers)
# ans = sum(prime_numbers)
# print(f"Sum of all prime numbers below {n} is {ans}")