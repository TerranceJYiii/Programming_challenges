#CodeForce Round 116a Tram

n = int(input())
passenger = 0
cap = 0
for i in range(n):
    o,i = map(int,input().split())
    passenger = passenger - o + i
    cap = max(cap, passenger)
print(cap)