from itertools import permutations
places = ["AlphaCentauri","Arbre","Faerun","Norrath","Snowdin","Straylight","Tambi","Tristram"]
book = dict()
for each in places:
    book[each] = dict()

def add_to_dict(section):
    a,b,dist = section[0], section[2],int(section[4])
    book[a][b] = dist
    book[b][a] = dist

with open("Task_Day9.txt","r") as infile:
    lines = infile.readlines()

for line in lines:
    add_to_dict(line.split())

# Task 9_1
minimum = 1000000000
# Task 9_2
maximum = 0
for each in permutations(places):
    temp = 0
    for i in range(7):
        temp += book[each[i]][each[i+1]]
    minimum = min(minimum,temp)
    maximum = max(maximum,temp)
print("Task 9_1 :",minimum)
print("Task 9_2 :",maximum)

