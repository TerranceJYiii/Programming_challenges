print("""Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 = 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10% ?""")

prime_list = [3,5,7]
pa = prime_list.append

# def is_prime(n):
#     limit = int(n**0.5)+1
#     for each in prime_list:
#         if each > limit:
#             break
#         elif n % each == 0:
#             return False
#     return True

def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


i = 1
ratio = 0.75
reach_condition = False
while ratio > 0.1:
    i += 1
    diff = 2 * i
    side = diff + 1 
    diagonal = side ** 2
    diagonal_list = []
    for _ in range(3):
        diagonal -= diff
        if is_prime(diagonal):
            pa(diagonal)
    ratio = len(prime_list)/(i*4+1)
    # print(side)

# print(prime_list, non_prime_list)
print(len(prime_list), i*4 + 1)
print(side)
