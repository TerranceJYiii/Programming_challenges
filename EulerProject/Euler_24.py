print("""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?""")
from itertools import permutations
def Permutation(n):
    if n == 1:
        return n
    else:
        return n*Permutation(n-1)
    
n = int(input("\nPlease provide the input \n"))
pernum = Permutation(n)
print(pernum)

N = int(input("\nPlease provide the input \n"))
while (N>pernum or N<=0):
    N = int(input("\nPlease provide the input \n"))

l = list(permutations(range(n)))
target = l[N-1]
print(target)

# print(permutatuionlist)
