"""To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029."""

row = 2947
column = 3029
current = 20151125


n = row+column-1 -1
final_index =(n/2) * (n+1) + column

index = 1
while index < final_index:
    current = (current * 252533) % 33554393
    index += 1

print(current)