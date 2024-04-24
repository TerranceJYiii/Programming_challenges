from turtle import pen


print("""Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?""")

pentagonallist = []
pa = pentagonallist.append
for n in range(1,3000):
    temp = n*(3*n-1)//2
    pa(temp)

l = len(pentagonallist)
print(l)
# print(pentagonallist[-1])
minima = 0

for a in range(l-1):
    for b in range(a+1,l):
        Pj = pentagonallist[a]
        Pk = pentagonallist[b]
        if Pk-Pj in pentagonallist: 
            # print("got-")
            # print(Pk,Pj,Pk-Pj,"-")
            if Pk+Pj in pentagonallist:
                # print('got+')
                # print(Pk,Pj,Pk+Pj,"+")
                if minima == 0:
                    minima = Pk-Pj
                else:
                    minima = min(minima, Pk-Pj)

print(minima)