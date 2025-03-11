with open("Task_Day10.txt","r") as infile:
    lines = infile.readlines()

bot = dict()
output = dict()
instructions = dict()

def add_to_bot(val, bot_no):
    if bot_no not in bot:
        bot[bot_no] = [val]
    else:
        bot[bot_no].append(val)

def pass_next(val,oup_bot):
    if oup_bot[0] == "bot":
        add_to_bot(val, oup_bot[1])
    else:
        output[oup_bot[1]] = val

for line in lines:
    each = line.split()
    if each[0] == "value":
        add_to_bot(each[1], each[-1])
    else:
        instructions[each[1]] = {"low":each[5:7], "high":each[10:12]}

# print(instructions)
# print(bot)
not_done = True
while not_done:
    for each in bot:
        if len(bot[each]) == 2:
            # print(each, bot[each])
            chips = bot[each]
            if "17" in chips and "61" in chips:
                print(each)
                not_done = False
                break
            else:
                ins = instructions[each]
                # print(ins)
                val1, val2 = bot[each]
                # print(val1, val2)
                if int(val1) > int(val2):
                    pass_next(val2, ins["low"])
                    pass_next(val1, ins["high"])
                else:
                    pass_next(val1, ins["low"])
                    pass_next(val2, ins["high"])
                bot[each] = []
            break

