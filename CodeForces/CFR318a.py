#CodeForce Round 318a Even Odds
from math import ceil

n,k = map(int,input().split())
mid = ceil(n/2)
if k <= mid:
    print(1+2*(k-1))
else:
    print((k-mid)*2)