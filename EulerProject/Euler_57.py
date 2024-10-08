print("""It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + 1/.......)))

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2
      
1 + 1/(2 + 1/2) = 7/5
      
1 + 1/(2 + 1/(2 + 1/2)) = 17/12

1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

 
The next three expansions are 99/70, 239/169, and 577/408, 

but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?""")

def process(a,b):
    a += 2 * b
    return b,a

def count_digit(n):
    return len(str(n))

ans = 0

a,b = 1,2
for i in range(1000):
    temp = a + b
    if count_digit(temp) > count_digit(b):
        ans += 1
    # print(f"1 + {a}/{b} = {temp}/{b}")
    a,b = process(a,b)

print(ans)