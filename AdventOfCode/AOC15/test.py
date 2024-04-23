from itertools import permutations

ls = list(map(list,permutations([1,2,3])))
for each in ls:
    for i in range(1,3):
        ls.remove(each[i:] + each[:i])

print(ls)
