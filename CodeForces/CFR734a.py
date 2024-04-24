#CodeForce Round 734a Anton and Danik

n = int(input())/2
data = input()

win = data.count("A")
if win > n:
    print("Anton")
elif win < n:
    print("Danik")
else:
    print("Friendship")