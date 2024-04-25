print("""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?""")

from math import sqrt

maxp = 0
maxima = 3
for p in range(12,1000):
    # print(p)
    numofsoln = 0
    for a in range(1,501):
        if a < p:
            for b in range(1,501):
                if a+b < p:
                    c = sqrt(a**2 + b**2)
                    if a+b+c == p:
                        # print(a,b,c)
                        numofsoln += 1
    
    if maxima < numofsoln:
        maxima = numofsoln
        maxp = p

print(maxp, maxima)

