#CodeForce Round 2a Winner

scorelist = {}
instruction_list = []
ia = instruction_list.append

n = int(input())

for i in range(n):
    name, strscore = input().split()
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
    maxima = -1000
    for ins in instruction_list:
        print(ins)
        if ins[0] in temp_ppl:
            if ins[0] not in temp_score:
                temp_score[ins[0]] = ins[1]
            else:
                temp_score[ins[0]] += ins[1]
            
            if temp_score[ins[0]] > maxima:
                winner = ins[0]
                maxima = ins[1]
                print(winner, maxima)
else:
    for ppl in scorelist:
        if scorelist[ppl] == realmax:
            winner = ppl
            break

print(winner)
