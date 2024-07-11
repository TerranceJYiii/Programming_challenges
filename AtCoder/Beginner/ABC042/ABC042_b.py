N, L = map(int,input().split())
ls = []
for i in range(N):
    ls.append(input())

ls = sorted(ls)
print("".join(ls))