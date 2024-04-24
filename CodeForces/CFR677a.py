#CodeForce Round 677a Vanya and Fence

w = 0
n,k = map(int,input().split())
person = list(map(int,input().split()))
for each in person:
    if each > k:
        w += 2
    else:
        w += 1
print(w) 
