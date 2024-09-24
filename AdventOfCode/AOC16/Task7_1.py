with open("Task_Day7.txt","r") as infile:
    lines = infile.readlines()

def check_valid(s):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]

def find_char(line,char):
    return [i for i in range(len(line)) if line[i] == char]

def check_in_substring(substring):
    for i in range(len(substring)-3):
        if check_valid(substring[i:i+4]):
            return True
    return False

ans = 0

for line in lines:
    open_sqb = find_char(line,"[")
    close_sqb = find_char(line,"]")
    num_of_sqb = len(open_sqb)

    fail = False
    for i in range(num_of_sqb):
        substring = line[open_sqb[i]+1:close_sqb[i]]
        fail = check_in_substring(substring)
        if fail:
            break
    if fail:
        # print(line, "is fail")
        continue

    substring = line[:open_sqb[0]]
    success = check_in_substring(substring)
    if success:
        ans += 1 
        # print(line, "is success")
        continue
    
    substring = line[close_sqb[-1]:]
    success = check_in_substring(substring)
    if success:
        ans += 1 
        # print(line, "is success")
        continue
    
    for i in range(num_of_sqb - 1):
        substring = line[close_sqb[i]:open_sqb[i+1]]
        success = check_in_substring(substring)
        if success:
            break
    if success:
        ans += 1
    #     print(line, "is success")
    # else:
    #     print(line, "is fail")
print(ans)