#CodeForce Round 133a HQ9+

instruction = [*"HQ9"]
code = input()
if any(c in code for c in instruction):
    print("YES")
else:
    print("NO")