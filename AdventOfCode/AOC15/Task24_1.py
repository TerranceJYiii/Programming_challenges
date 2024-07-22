from itertools import combinations

with open("Task_Day24.txt","r") as infile:
    lines = infile.readlines()

def quantum_entangle(comb):
    temp = 1
    for each in comb:
        temp *= each
    return temp

items = []
for line in lines:
    items.append(int(line))

target = sum(items)//4      # Task23_1, divide = 3; Task23_2, divide = 4;
print(target)

ans = []
i = 1
while len(ans) == 0:
    i += 1
    for comb in combinations(items,i):
        if sum(comb) == target:
            ans.append(quantum_entangle(comb))

print(min(ans))
