#CodeForce Round 231a Team

n = int(input())
ans = 0
for i in range(n):
    string = input()
    if string.count("1") > 1:
        ans += 1
print(ans)