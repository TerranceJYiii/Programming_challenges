with open("Task_Day4.txt","r") as infile:
    lines = infile.readlines()

num_of_card = [1]*len(lines)
card_index = 0

for line in lines:
    line = line.replace(":", "|")
    data = line.split("|")
    winning = data[1].strip().split()
    own = data[2].strip().split()
    
    num_of_win = 0
    for each in winning:
        if each in own:
            num_of_win += 1

    for i in range(card_index + 1, card_index + 1 + num_of_win):
        num_of_card[i] += num_of_card[card_index]
    card_index += 1

print(num_of_card)
print(sum(num_of_card))