#CodeForce Round 2a Winner

scorelist = {}
instruction_list = []
ia = instruction_list.append

n = int(input("Please enter the number of test case for 2a : Winner\n"))

for i in range(n):
    name, strscore = input("Please give input for 2a : Winner\n").split()
    score = int(strscore)
    ia([name, score])
    if name not in scorelist:
        scorelist[name] = score
    else:
        scorelist[name] += score
 
ls = list(scorelist[ppl] for ppl in scorelist)
realmax = max(ls)
 
if ls.count(realmax)> 1:
    temp_ppl = []
    for ppl in scorelist:
        if scorelist[ppl] == realmax:
            temp_ppl.append(ppl)
 
    temp_score = {}
    maxima = realmax
    for ins in instruction_list:
        if ins[0] in temp_ppl:
            if ins[0] not in temp_score:
                temp_score[ins[0]] = ins[1]
            else:
                temp_score[ins[0]] += ins[1]
            
            if temp_score[ins[0]] >= maxima:
                winner = ins[0]
                break
 
else:
    for ppl in scorelist:
        if scorelist[ppl] == realmax:
            winner = ppl
            break
 
 
print(winner)
