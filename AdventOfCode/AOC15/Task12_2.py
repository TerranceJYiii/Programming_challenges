with open("Task_Day12.txt","r") as infile:
    lines = infile.readlines()
line = lines[0]

# bracket = 0
# bracket_list = []
# for i in range(len(line)):
#     if line[i] == "{":
#         if bracket == 0:
#             bracket_list.append([i])
#         bracket += 1
#     elif line[i] == "}":
#         if bracket == 1:
#             bracket_list[-1].append(i)
#         bracket -= 1
# # print(bracket_list)

# ans = 0
# temp = ""  
# l = len(bracket_list)
# for i in range(l):
#     if "red" not in line[bracket_list[i][0]:bracket_list[i][1]]:
#         temp = ""
#         for each in line[bracket_list[i][0]:bracket_list[i][1]]:
#             if each.isdigit() or each == "-":
#                 temp += each
#             else:
#                 if temp == "":
#                     continue
#                 else:
#                     ans += int(temp)
#                     temp = ""
#     if i < l-1 and "red" not in line[bracket_list[i][1]:bracket_list[i+1][0]]:
#         temp = ""
#         for each in line[bracket_list[i][1]:bracket_list[i+1][0]]:
#             if each.isdigit() or each == "-":
#                 temp += each
#             else:
#                 if temp == "":
#                     continue
#                 else:
#                     ans += int(temp)
#                     temp = ""

# print(ans)


# cheat
import re
import json

def hook(obj):
  if "red" in obj.values(): return {}
  else: return obj
stuff = str(json.loads(line, object_hook=hook))
print (sum(map(int, re.findall("-?[0-9]+", stuff))))