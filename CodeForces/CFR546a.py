#CodeForce Round 546a Soldier and Bananas

k,n,w = map(int, input().split())
needed_money = (w/2)*(w+1)*k
borrow = int(needed_money - n)
if borrow < 0:
    print(0)
else:
    print(borrow)