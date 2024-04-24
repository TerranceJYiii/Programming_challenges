#CodeForce Round 4c Registration system

n = int(input())
seta = set()
su = seta.add

for i in range(n):
    name = input()
    if name not in seta:
        su(name)
        print("OK")
    else:
        n = 1
        newname = name + str(n)
        while newname in seta:
            n += 1
            newname = name + str(n)
        su(newname)
        print(newname)
