from itertools import permutations
people = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory", "me"]
book = dict()
book["me"] = dict()
for i in range(8):
    book[people[i]] = {"me":0}
    book["me"][people[i]] = 0

with open("Task_Day13.txt","r") as infile:
    lines = infile.readlines()

for line in lines:
    line = line.split()
    person_A, person_B, posneg, happiness = line[0], line[-1][:-1], line[2], int(line[3])
    if posneg == "lose":
        happiness = -happiness
    book[person_A][person_B] = happiness

# print(book)

lista = list(map(list,permutations(people)))
for each in lista:
    for i in range(1,9):
        lista.remove(each[i:] + each[:i])

# print(len(lista))

# Task 13_1
maxima = 0
for each in lista:
    temp = 0
    for i in range(8):
        temp += book[each[i]][each[i+1]] + book[each[i]][each[i-1]]
    temp += book[each[8]][each[0]] + book[each[8]][each[7]]
    maxima = max(maxima,temp)
print("Task 13_2 :",maxima)
