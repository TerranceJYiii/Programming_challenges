with open("Task_Day7.txt","r") as infile:
    lines = infile.readlines()

def find_char(line,char):
    return [i for i in range(len(line)) if line[i] == char]

def add_to_search(sub):
    a,b,c = sub
    if a == c and a != b:
        to_search.append(b+a+b)

def extract_tosearch(substring):
    for i in range(len(substring) - 2):
        add_to_search(substring[i:i+3])

def search_tosearch(substring):
    for each in to_search:
        if each in substring:
            return True
    return False
ans = 0

for line in lines:
    to_search = []
    open_sqb = find_char(line,"[")
    close_sqb = find_char(line,"]")
    num_of_sqb = len(open_sqb)

    fail = False
    for i in range(num_of_sqb):
        substring = line[open_sqb[i]+1:close_sqb[i]]
        extract_tosearch(substring)

    substring = line[:open_sqb[0]]
    success = search_tosearch(substring)
    if success:
        ans += 1 
        # print(line, "is success")
        continue
    
    substring = line[close_sqb[-1]:]
    success = search_tosearch(substring)
    if success:
        ans += 1 
        # print(line, "is success")
        continue
    
    for i in range(num_of_sqb - 1):
        substring = line[close_sqb[i]:open_sqb[i+1]]
        success = search_tosearch(substring)
        if success:
            break
    if success:
        ans += 1
    #     print(line, "is success")
    # else:
    #     print(line, "is fail")
print(ans)