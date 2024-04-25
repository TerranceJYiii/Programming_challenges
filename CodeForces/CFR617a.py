#CodeForce Round 617a Elephant

n = int(input())
steps = n//5
if n%5:
    print(steps+1)
else:
    print(steps)