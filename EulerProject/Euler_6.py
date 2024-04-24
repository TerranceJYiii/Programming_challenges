print(""""Project Euler 6: Sum square difference
The sum of the squares of the first ten natural numbers is 385,
The square of the sum of the first ten natural numbers is 3025,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
""")

n = int(input('\nPlease provide the input\n'))
all_num = list(range(1,n+1))
sum_of_square = 0
for i in all_num:
    sum_of_square += i ** 2
total = sum(all_num)
square_of_sum = total ** 2

print(sum_of_square)
print(square_of_sum)

ans = square_of_sum - sum_of_square
print(f"Answer is {ans}")