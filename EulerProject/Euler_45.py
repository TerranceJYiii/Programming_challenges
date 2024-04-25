print("""Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal. """)

from math import sqrt

def isTriangle(n):
    tri = (sqrt((8*n) + 1) - 1) / 2
    if tri % 1 == 0:
        return True
    else:
        return False
    
def isPentagonal(n):
    penta = (sqrt((24*n) + 1) + 1) / 6
    if penta % 1 == 0:
        return True
    else:
        return False

hexlist = []
ha = hexlist.append
for n in range(100000):
    hexagonal = n*(2*n - 1)
    ha(hexagonal)

# print(hexlist)
# print(hexlist.index(40755))

for i in hexlist:
    if isTriangle(i):
        if isPentagonal(i):
            print(i)