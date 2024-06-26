print("""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
""")

maxima = 0
for n in range(1,1000001):
    print(n)
    i = 1
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        i += 1
    maxima = max(maxima, i)

print(maxima)

for n in range (1000001, 1, -1):
    print(n)
    i = 1
    j = n
    while j != 1:
        if j%2 == 0:
            j = j/2
        else:
            j = 3*j + 1
        i += 1
    if i == maxima:
        print(n)
        break
    