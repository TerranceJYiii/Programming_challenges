#CodeForce Round 160a Twins

n = int(input())
ls = sorted(list(map(int, input().split())))
twin = sum(ls)
me = twin / 2
for i in range(n):
    coin = ls.pop()
    twin -= coin
    if me > twin:
        print(i+1)
        break