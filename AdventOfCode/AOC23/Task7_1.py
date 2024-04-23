with open("Task_Day7.txt","r") as infile:
    lines = infile.readlines()

order = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "T":8, "J":9, "Q":10, "K":11, "A":12}

Five_oak = {}
Four_oak = {}
Full_house = {}
Three_oak = {}
Two_pair = {}
One_pair = {}
High_card = {}

def count(card):
    num_of_card = []
    set_card = set([*card])
    for each in set_card:
        num_of_card.append(card.count(each))
    return sorted(num_of_card)

def seek_value(card):
    value = 0
    for each in card:
        value *= 100
        value += order[each]
    return value

for line in lines:
    card, bet = line.split()
    num_of_card = count(card)
    if num_of_card == [5]:
        Five_oak[card] = int(bet)
    elif num_of_card == [1,4]:
        Four_oak[card] = int(bet)
    elif num_of_card == [2,3]:
        Full_house[card] = int(bet)
    elif num_of_card == [1,1,3]:
        Three_oak[card] = int(bet)
    elif num_of_card == [1,2,2]:
        Two_pair[card] = int(bet)
    elif num_of_card == [1,1,1,2]:
        One_pair[card] = int(bet)
    else:
        High_card[card] = int(bet)

all_hand = [High_card,One_pair,Two_pair,Three_oak,Full_house,Four_oak,Five_oak]

ans = 0
i = 1
for each_set in all_hand:
    temp_set = {}
    for card in each_set:
        temp_set[card] = seek_value(card)
    temp_set = dict(sorted(temp_set.items(), key=lambda x:x[1]))
    for card in temp_set:
        ans += i * each_set[card]
        i += 1
print(ans)
