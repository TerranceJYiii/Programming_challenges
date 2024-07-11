N = int(input())
L = map(int,input().split())

L = sorted(L)[::2]
print(sum(L))
