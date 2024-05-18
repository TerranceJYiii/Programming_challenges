from itertools import combinations

container = [7, 10, 11, 18, 18, 21, 22, 24, 26, 32, 36, 40, 40, 42, 43, 44, 46, 47, 49, 50]
volume = 150

# create min and max
temp = 0
for i in range(len(container)):
    temp += container[i]
    if temp >= volume:
        max = i+1
        break

temp = 0
for j in range(len(container)):
    temp += container[-j-1]
    if temp >= volume:
        min = j+1
        break

# print(min,max)

ans = 0
# Task 1
# for i in range(min,max+1):      
#     possible = combinations(container,i)
#     for each in possible:
#         if sum(each) == 150:
#             ans += 1

# Task 2
i = min
possible = combinations(container,i)
for each in possible:
    if sum(each) == 150:
        ans += 1

print(ans)