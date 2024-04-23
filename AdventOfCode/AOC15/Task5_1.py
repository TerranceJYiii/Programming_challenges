with open("Task_Day5.txt","r") as infile:
    lines = infile.readlines()

required = ["aa","bb","cc",'dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
banned = ['ab','cd','pq','xy']
vowel = ['a','e','i','o','u']
ans = 0
for line in lines:
    if any(ban in line for ban in banned):
        continue
    if not any(req in line for req in required):
        continue
    counting = 0
    for each in vowel:
        counting += line.count(each)
    if counting >2:
        ans += 1
            
print(ans)