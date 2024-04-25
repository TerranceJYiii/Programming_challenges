print("""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.""")

from itertools import permutations

double = ['2', '4', '6', '8', '0']

plist = []
pa = plist.append
p = permutations("9876543210")
for each in p:
    temp = "".join(each)
    # temp = '1406357289'
    # print(temp)
    if temp[0] != '0':
        if temp[3] in double:
            iter2 = int(temp[2:5])
            if iter2 % 3 == 0:
                if temp[5] == '5' or temp[5] == '0':
                    iter4 = int(temp[4:7])
                    if iter4 % 7 == 0:
                        iter5 = int(temp[5:8])
                        if iter5 % 11 == 0:
                            iter6 = int(temp[6:9])
                            if iter6 % 13 == 0:
                                iter7 = int(temp[7:])
                                if iter7 % 17 == 0:
                                    pa(int(temp))
                                    # print(iter2,iter4,iter5,iter6,iter7)


print(plist)
print(sum(plist))