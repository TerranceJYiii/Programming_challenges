#CodeForce Round 266a Stones on the Table

n = int(input())
str = input()
past = ""
now = ""
ans = 0
for each in str:
    past = now
    now = each
    if past == now:
        ans += 1
print(ans)