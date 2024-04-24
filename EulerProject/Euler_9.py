print(""""Project Euler 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
""")

import math


a = 3
b = 4 
c = (a**2 + b**2)**0.5
d = a+b+c
while d!=1000:
    b += 1
    for num in range(1,b):
        temp_c = (num**2 + b**2) ** 0.5
        result = temp_c.is_integer()
        if result:
            a = num
            c = temp_c
            d = a+b+c
            break
    d = a+b+c
print(a)
print(b)
print(c)
ans = a*b*c
print(ans)