print("""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000? """)

n =  int(input('\nPlease provide the input\n'))
num = 2**n
val = str(num)
i = len(val)
sum = 0
for each in range(i): 
    sum += int(val[each])

print(sum)