#CodeForce Round 271a Beautiful Year

def check_year(y):
    if len(set([*str(y)])) < 4:
        return False
    return True

y = int(input()) + 1
while not check_year(y):
    y += 1
print(y)
