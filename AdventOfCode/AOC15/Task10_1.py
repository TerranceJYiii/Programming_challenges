question = "1321131112"
# Task 10_1 : 40, Task 10_1 : 50
for _ in range(50):
    nextq = []
    temp = question[0]
    i = 0
    for char in question:
        if char == temp:
            i += 1
        else:
            nextq.append(str(i) + temp)
            temp = char
            i = 1
    nextq.append(str(i) + temp)
    question = "".join(nextq)
    # print(question)
print(len(question))

