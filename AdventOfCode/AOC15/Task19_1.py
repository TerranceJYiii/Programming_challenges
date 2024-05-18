with open("Task_Day19.txt","r") as infile:
    lines = infile.readlines()

input_line = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

ans = []
for line in lines:
    key, x, value = line.split()
    len_of_key = len(key)
    indexes = [i for i in range(len(input_line)) if input_line[i: i+len_of_key] == key]
    for each in indexes:
        ans.append(input_line[:each] + value + input_line[each+len_of_key:])

print(len(set(ans)))

# ls = [i for i in range(len(input_line)) if input_line[i:i+len(key)] == key]
# print(ls)
