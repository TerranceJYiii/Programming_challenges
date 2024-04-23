def process_line(ori_line):
    l = len(ori_line)
    temp = ""
    for i in range(l):
        char = ori_line[i]
        if char.isdigit():
            temp += char
            break
        elif char not in spell:
            continue
        else:
            if ori_line[i:i+3] == "one":
                temp += "1"
                break
            elif ori_line[i:i+3] == "two":
                temp += "2"
                break
            elif ori_line[i:i+5] == "three":
                temp += "3"
                break
            elif ori_line[i:i+4] == "four":
                temp += "4"
                break
            elif ori_line[i:i+4] == "five":
                temp += "5"
                break
            elif ori_line[i:i+3] == "six":
                temp += "6"
                break
            elif ori_line[i:i+5] == "seven":
                temp += "7"
                break
            elif ori_line[i:i+5] == "eight":
                temp += "8"
                break
            elif ori_line[i:i+4] == "nine":
                temp += "9"
                break
            else:
                continue
    
    for j in range(l-1,-1,-1):
        char = ori_line[j]
        if char.isdigit():
            temp += char
            break
        elif char not in spell_end:
            continue
        else:
            if ori_line[j-2:j+1] == "one":
                temp += "1"
                break
            elif ori_line[j-2:j+1] == "two":
                temp += "2"
                break
            elif ori_line[j-4:j+1] == "three":
                temp += "3"
                break
            elif ori_line[j-3:j+1] == "four":
                temp += "4"
                break
            elif ori_line[j-3:j+1] == "five":
                temp += "5"
                break
            elif ori_line[j-2:j+1] == "six":
                temp += "6"
                break
            elif ori_line[j-4:j+1] == "seven":
                temp += "7"
                break
            elif ori_line[j-4:j+1] == "eight":
                temp += "8"
                break
            elif ori_line[j-3:j+1] == "nine":
                temp += "9"
                break
            else:
                continue
    
    return temp
            

spell = ["o", "t", "f", "s", "e", "n"]
spell_end = ["e", "o", "r", "x", "n", "t"]

with open("Task_Day1.txt","r") as infile:
    lines = infile.readlines()

sum = 0

for line in lines:
    temp = process_line(line)
    # print(line, temp)
    sum += int(temp)
    
print(sum)