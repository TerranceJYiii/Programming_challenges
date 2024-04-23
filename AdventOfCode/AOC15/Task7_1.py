with open("Task_Day7.txt","r") as infile:
    lines = infile.readlines()

# ins = [in1 op in2]
def work(inputs,outputs):
    # print("work")
    if len(inputs) == 1:
        datas[outputs] = datas[inputs[0]]
        return True
    elif len(inputs) == 2:
        return conduct(inputs[1],inputs[0],outputs)
    elif len(inputs) == 3:
        if (inputs[0] in datas or inputs[0].isdigit()) and (inputs[2] in datas or inputs[2].isdigit()):
            return conduct(inputs[0],inputs[1],outputs,inputs[2])
        else:
            return False
    return False

def conduct(in1,op,output,in2 = "0"):
    # print("conduct")
    
    if not in1.isdigit():
        in1 = int(datas[in1])
    else:
        in1 = int(in1)
    
    if not in2.isdigit():
        in2 = int(datas[in2])
    else:
        in2 = int(in2)

    if op == "AND":
        datas[output] = in1 & in2
    elif op == "OR":
        datas[output] = in1 | in2
    elif op == "LSHIFT":
        datas[output] = in1 << in2
    elif op == "RSHIFT":
        datas[output] = in1 >> in2
    elif op == "NOT":
        datas[output] = 65535 - in1
    return True
         
instruction = dict() #{out : [in1 op in2]}
datas = dict()      #{line : data}

for line in lines:
    line_ab,line_c = line.strip().split("->")
    line_c = line_c.strip()
    instruction[line_c] = line_ab.split()
    if len(instruction[line_c]) == 1 and instruction[line_c][0].isdigit():
        datas[line_c] = instruction[line_c][0]
        instruction.pop(line_c)

datas["b"] = 956
# count = 0
while "a" not in datas:
    # print(datas)
    # print("iterdone",count)
    for line_c in instruction:
        if any(wire in datas for wire in instruction[line_c]):
            if work(instruction[line_c],line_c):    #if work successful
                # count += 1
                pass
        
print(datas["a"])