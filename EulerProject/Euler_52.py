print("""It can be seen that the number, 125784, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. """)

from itertools import permutations

for i in range(100001,333333):
    ls = list(map("".join,list(permutations(str(i)))))
    if str(2*i) in ls:
        if str(3*i) in ls:
            if str(4*i) in ls:
                if str(5*i) in ls:
                    if str(6*i) in ls:
                        print(i)
                        break 