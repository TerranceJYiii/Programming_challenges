print("""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.""")

def extract(val):
    if val <= 9:
        return val**5
    else:
        rem = val%10
        return rem**5 + extract(val//10)

def check(val):
    st = str(val)
    for i in range(2,10):
        si = str(i)
        if si in st and val < i**5:
            return False
    return True
        
anslist = []

for i in range(2,200000): #200000 is enough
    print(i)
    if check(i):
        if extract(i) == i:
            anslist.append(i)

print(anslist)