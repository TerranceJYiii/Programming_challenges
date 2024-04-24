#CodeForce Round 3a Shortest path of the king

hor = "abcdefgh"

start = input("Please give input for 3a : Shortest path of the king\n")
end = input("Please give input for 3a : Shortest path of the king\n")

lr = hor.index(end[0]) - hor.index(start[0])
ud = int(end[1]) - int(start[1])

hordir = "R" if lr > 0 else "L"
verdir = "U" if ud > 0 else "D"

abslr = abs(lr)
absud = abs(ud)
steps = max(abslr,absud)
print(steps)
adj = min(abslr,absud)

if absud > abslr:
    for i in range(steps):
        if adj > 0:
            print(hordir + verdir)
            adj -= 1
        else:
            print(verdir)
else:
    for i in range(steps):
        if adj > 0:
            print(hordir + verdir)
            adj -= 1
        else:
            print(hordir)