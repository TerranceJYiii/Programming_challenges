with open("Task_Day4.txt","r") as infile:
    lines = infile.readlines()

correct_alpha = "abcdefghijklmnopqrstuvwxyz"
ans = "northpole object storage "

def shift(phrases, id):
    name = []
    shift = id % 26
    for each in phrases:
        for char in each:
            name.append(correct_alpha[(correct_alpha.index(char) + shift) % 26])
        name.append(" ")

    name = "".join(name)
    if name == ans:
        print(id, "".join(name))


for line in lines:
    phrases = line.split("-")
    id,checksum = phrases.pop(-1).split("[")

    name = "".join(phrases)
    alphabet = set(name)
    alphabet_count = {}
    for each in alphabet:
        count = name.count(each)
        if count not in alphabet_count:
            alphabet_count[count] = each
        else:
            alphabet_count[count] += each
    x = sorted(alphabet_count,reverse=True)
    
    check = ""
    for each in x:
        check += "".join(sorted(alphabet_count[each]))
    if check[:5] == checksum[:5]:
        shift(phrases,int(id))
