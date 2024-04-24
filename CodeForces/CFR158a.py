#CodeForce Round 158a Next Round

n, k = map(int,input().split())
rank = list(map(int,input().split()))
ans = k
for i in range(k,n):
    if rank[i] == rank[k-1]:
        ans += 1
    else:
        break
for j in range(ans-1,-1, -1):
    if rank[j] < 1:
        ans -= 1
    else:
        break
print(ans)
