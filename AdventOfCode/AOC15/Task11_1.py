alphabet = "abcdefghijklmnopqrstuvwxyz"
repeated = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
password = "vzbxkghb"
banned = ["i","o","l"]

# Task11_1 and Task11_2 
def increment(password):
    if password[-1] != "z":
        return password[:-1] + alphabet[alphabet.index(password[-1])+1]
    else:
        return increment(password[:-1]) + 'a'

pairs = 0
while 1:
    password = increment(password)
    if any(ban in password for ban in banned):
        continue

    streak = False
    for i in range(6):
        if password[i:i+3] in alphabet:
            streak = True
            break
    if not streak:
        continue
    
    pair = 0
    for each in repeated:
        pair += password.count(each)
        if pair > 1:
            pairs += 1
            print(f"Task 11_{pairs} : {password}")
            break
    if pairs > 1:
        break
