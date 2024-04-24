#CodeForce Round 580a Kefa and First Steps

n = input()
step = list(map(int,input().split()))
pre = 0
i = 0
m = 0
for each in step:
    if each >= pre:
        i += 1
    else:
        m = max(i,m)
        i = 1
    pre = each
m = max(i,m)
print(m)