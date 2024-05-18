data = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

with open("Task_Day16.txt","r") as infile:
    lines = infile.readlines()

def build_dict(line):
    temp = dict()
    line = line.split()
    for i in range(1, len(line)//2):
        char, num = line[2*i:2*(i+1)]
        if char[-1] == ":":
            char = char[:-1]
        if num[-1] == ",":
            num = num[:-1]
        temp[char] = int(num)
    aunty = int(line[1][:-1])
    return aunty, temp

def Task_1(aunty_dict):
    if all(aunty_dict[char] == data[char] for char in aunty_dict):
        return True
    return False

def Task_2(aunty_dict):
    for each in aunty_dict:
        if each == "cats" or each == "trees":
            if aunty_dict[each] <= data[each]:
                return False
        elif each == "pomeranians" or each == "goldfish":
            if aunty_dict[each] >= data[each]:
                return False
        else:
            if aunty_dict[each] != data[each]:
                return False
    return True

answer = []

for line in lines:
    aunty, aunty_dict = build_dict(line)
    # if Task_1(aunty_dict):
    #     answer.append(aunty)
    if Task_2(aunty_dict):
        answer.append(aunty)


print(answer)