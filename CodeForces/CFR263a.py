#CodeForce Round 263a Beautiful Matrix

for i in range(5):
    row = input()
    if "1" in row:
        ans = abs(i-2)
        column = row.split()
        for j in range(5):
            if column[j] == "1":
                ans += abs(j-2)
                break
print(ans)
        