print("""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum. """)

pandig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pa = pandig_list.append
anslist = []
aa = anslist.append

def checkpandig(a,b):
    stra = str(a)
    strb = str(b)
    strc = str(a*b)
    finalstr = stra + strb +strc
    if len(finalstr) != 9:
        return False
    if "0" in finalstr:
        return False
    for char in finalstr:
        if finalstr.count(char) > 1:
            return False
    return True

for i in range(10,10000):
    st = str(i)
    if st.count(st[0]) > 1:
        continue
    elif st.count(st[1]) > 1:
        continue
    elif st[1] == "0" :
        continue
    elif i > 100 and st[2] == "0":
        continue
    pa(i)

for each in pandig_list:
    for anot in pandig_list:
        if checkpandig(each, anot):
            # print(each, anot, each*anot)
            aa(each*anot)

anslist.sort()
print(anslist)
for ans in anslist:
    n = anslist.count(ans) 
    if n > 1:
        for i in range(n-1):
            anslist.remove(ans)

print(anslist)
print(sum(anslist))
