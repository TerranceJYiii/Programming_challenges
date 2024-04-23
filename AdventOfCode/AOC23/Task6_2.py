with open("Task_Day6.txt","r") as infile:
    lines = infile.readlines()

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

# solved = False
# for i in range(0,time,10):
#     if not solved and (i*(time-i)) > distance:
#         for j in range(i-10, i+1):
#             if (j*(time-j)) > distance:
#                 success = time - 2*j + 1
#                 print(success)
#                 solved = True
#                 break


for i in range(time):
    if (i*(time-i)) > distance:
        success = time - 2*i + 1
        print(success)
        break