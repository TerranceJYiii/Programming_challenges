print(""""Project Euler 5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
""")

n = int(input('\nPlease provide the input\n'))
current_list = list(range(n, 1, -1)) #Original list, need to remove all number which is factor of others
temp_list = list(range(n, 1, -1)) #List to determine a number is factor of others or not
remove_list  = [] #List to store number which is factors of others

print(current_list)

for i in current_list:
    for factor in temp_list:
        if i % factor == 0 and i != factor: #Check whether this number has factors and add to remove list
            remove_list.append(factor)
            if factor in current_list: #Remove the number which is a factor from original list
                current_list.remove(factor)

print(current_list)
print(temp_list)
print(remove_list)

new_list = [] #List to store first appear number from remove list
divide_list = [] #List to store appeared number from remove list
for i in remove_list:
    if i not in new_list:
        new_list.append(i)
    else:
        divide_list.append(i)
print(new_list)
print(divide_list)

extra_list = []
for each in divide_list:
    if each == 4:
        extra_list.append(2)
    elif each == 6:
        extra_list.append(2)
        extra_list.append(3)
    elif each == 8:
        extra_list.append(4)
    elif each == 9:
        extra_list.append(3)
    elif each == 10:
        extra_list.append(2)
        extra_list.append(5) 
print(extra_list)
#Answer = multiply everything remain in current list divide by divide list
ans = 1
for each in current_list:
    ans *= each
for every in divide_list:
    ans /= every
for ext in extra_list:
    ans *= ext
print(f"Answer = {ans}")
