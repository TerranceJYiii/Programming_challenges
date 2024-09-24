from itertools import combinations
from math import factorial

# fac_ls = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
# def check_factorial(n):
#     if n < len(fac_ls):
#         return fac_ls[n]
#     else:
#         l = len(fac_ls)
#         while n >= l:
#             fac_ls.append(fac_ls[-1]*l)
#             l += 1
#         return fac_ls[n]

N = int(input())
skewers = []

for _ in range(N):
    a,b = map(int,input().split())
    skewers.append((a,b))

ans = 0

comb = combinations(range(N),2)
for each in comb:
    s1,s2 = each
    meat = skewers[s1][0] + skewers[s2][0]
    vege = skewers[s1][1] + skewers[s2][1]
    ans += factorial(meat+vege)/ (factorial(meat) * factorial(vege))

print(int(ans)%1000000007)