import numpy as np
from itertools import combinations

with open("Task_Day11.txt","r") as infile:
    lines = infile.readlines()

universe = np.array([])
for i in range(len(lines)):
    lines[i] = [*lines[i]]
    lines[i].pop()
    universe = np.append(universe,lines[i])

universe.shape = (140,140)

empty_row = []
empty_col = []
for i in range(140):
    if "#" not in universe[i]:
        empty_row.append(i+1)
temp = np.transpose(universe)
for j in range(140):
    if "#" not in temp[j]:
        empty_col.append(j+1)
    
for each_r in empty_row[::-1]:
    universe = np.insert(universe,each_r,".",axis=0)
for each_c in empty_col[::-1]:
    universe = np.insert(universe,each_c,".",axis=1)

coordinates = []
rows,cols = len(universe),len(universe[0])
for i in range(rows):
    for j in range(cols):
        if universe[i][j] == "#":
            coordinates.append((i,j))

comls = combinations(coordinates,2)
# print(list(comls))
ans = 0
for each in comls:
    ans += (abs(each[1][0]- each[0][0]) + abs(each[1][1]- each[0][1]))
print(ans)