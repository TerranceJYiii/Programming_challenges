print("""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way? """)

n = int(input('\nPlease provide the input\n'))
while n%2 == 0:
    n = int(input('\nPlease provide the input\n'))
mid = n//2

array = []
for i in range(n):
    array.append([0]*n)

def addvalue(x,y,value):
    array[x][y] = value
    return value + 1

value = 1
x = mid
y = mid
value = addvalue(x,y,value)
side = 2

while value < n**2:
    y += 1
    value = addvalue(x,y,value)

    for i in range(side-1):
        x += 1
        value = addvalue(x,y,value)
    
    for j in range(side):
        y -= 1
        value = addvalue(x,y,value)

    for k in range(side):
        x -= 1
        value = addvalue(x,y,value)

    for l in range(side):
        y += 1
        value = addvalue(x,y,value)

    side += 2
    

# for i in range(n):
#     print(array[i])

sum = 0
for i in range(n):
    sum += array[i][i]
for k in range(n):
    sum += array[k][n-1-k]
print(sum)