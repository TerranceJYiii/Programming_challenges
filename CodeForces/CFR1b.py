#CodeForce Round 1b Spreadsheets
import re

rs = re.search
rf = re.findall
rp = re.split

ALPHABET = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

def num_to_char(i):
    char = ""
    while(i>0):
        i-=1
        char = ALPHABET[(i%26)] + char
        i = i//26 
    return char

def char_to_num(c):
    num = 0
    for each in c:
        num *= 26
        num += ALPHABET.index(each) + 1
    return str(num)        

def convert_format(cs):
    if rs("R.*\dC.*\d",cs):
        ls = rp("\D",cs)
        return(num_to_char(int(ls[2])) + ls[1])
    else:
        ls = rp("\d",cs)
        return("R" + "".join(rf("\d",cs)) + "C" + char_to_num(ls[0]))

n = int(input("Please enter the number of test case for 1b :Spreadsheets\n"))
for i in range(n):
    cs = input("Please give input for 1b :Spreadsheets\n")
    print(convert_format(cs))