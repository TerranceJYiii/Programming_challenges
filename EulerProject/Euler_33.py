print("""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator. """)

def havesame(u, d):
    stringu = str(u)
    stringd = str(d)
    if stringu[0] == stringd[0]:
        return True
    elif stringu[0] == stringd[1]:
        return True
    elif stringu[1] == stringd[0]:
        return True
    elif stringu[1] == stringd[1]:
        return True
    else:
        return False

def iscuriousFraction(u,d):
    ans1 = u/d
    stringu = str(u)
    stringd = str(d)
    if stringu[0] == stringd[0]:
        newu = int(stringu[1])
        newd = int(stringd[1])
    elif stringu[0] == stringd[1]:
        newu = int(stringu[1])
        newd = int(stringd[0])
    elif stringu[1] == stringd[0]:
        newu = int(stringu[0])
        newd = int(stringd[1])
    elif stringu[1] == stringd[1]:
        newu = int(stringu[0])
        newd = int(stringd[0])

    if newd == 0:
        return False
    ans2 = newu/newd
    if ans1 == ans2:
        return True
    else:
        return False

anslistup = []
anslistdown = []

for up in range(10,100):
    for down in range(up + 1,101):
        if up % 10 == 0 and down % 10 == 0:
            continue
        elif up % 11 == 0 and down % 11 == 0:
            continue
        else:
            if havesame(up,down):
                if iscuriousFraction(up,down):
                    anslistup.append(up)
                    anslistdown.append(down)

print(anslistup)
print(anslistdown)

