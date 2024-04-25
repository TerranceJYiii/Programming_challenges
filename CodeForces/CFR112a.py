#CodeForce Round 112a Petya and Strings

line1 = input().lower()
line2 = input().lower()
ans = 0
if line1 == line2:
    print(ans)
else:
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            continue
        elif line1[i] > line2[i]:
            ans = 1
            break
        else:
            ans = -1
            break
    print(ans)