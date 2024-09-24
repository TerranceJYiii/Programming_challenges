with open("Task_Day4.txt","r") as infile:
    lines = infile.readlines()

ans = 0

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
        ans += int(id)

print(ans)