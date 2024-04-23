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
        empty_row.append(i)
temp = np.transpose(universe)
for j in range(140):
    if "#" not in temp[j]:
        empty_col.append(j)

expand_factor = 1000000

coordinates = []
rows,cols = len(universe),len(universe[0])
for i in range(rows):
    for j in range(cols):
        if universe[i][j] == "#":
            coordinates.append((i,j))

comls = combinations(coordinates,2)
ans = 0
for each in comls:
    x1,y1 = each[0]
    x2,y2 = each[1]
    dist = (abs(x2-x1) + abs(y2-y1))
    for er in empty_row:
        if (er > x1 and er < x2) or (er > x2 and er < x1):
            dist += expand_factor - 1
    for ec in empty_col:
        if (ec > y1 and ec < y2) or (ec > y2 and ec < y1):
            dist += expand_factor - 1
    ans += dist
print(ans)