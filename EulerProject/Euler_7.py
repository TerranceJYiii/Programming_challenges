print(""""Project Euler 7: 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
""")

n = int(input('\nPlease provide the input\n'))
total_prime_num = 1
num = 3
prime_num_list = [2]
while total_prime_num < n:
    for i in range(len(prime_num_list)):
        current_i = prime_num_list[i]
        if num % current_i == 0:
            num += 1
            break
        if i == len(prime_num_list)-1:
            prime_num_list.append(num)
            total_prime_num +=1
            num +=1


print(f"The {n}th prime number is {prime_num_list[-1]}")