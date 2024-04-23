from itertools import permutations
people = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]
book = dict()
for each in people:
    book[each] = dict()

with open("Task_Day13.txt","r") as infile:
    lines = infile.readlines()

for line in lines:
    line = line.split()
    person_A, person_B, posneg, happiness = line[0], line[-1][:-1], line[2], int(line[3])
    if posneg == "lose":
        happiness = -happiness
    book[person_A][person_B] = happiness

print(book)

lista = list(map(list,permutations(people)))
for each in lista:
    for i in range(1,8):
        lista.remove(each[i:] + each[:i])

# print(len(lista))

# Task 13_1
maxima = 0
for each in lista:
    temp = 0
    for i in range(7):
        temp += book[each[i]][each[i+1]] + book[each[i]][each[i-1]]
    temp += book[each[7]][each[0]] + book[each[7]][each[6]]
    maxima = max(maxima,temp)
print("Task 13_1 :",maxima)
