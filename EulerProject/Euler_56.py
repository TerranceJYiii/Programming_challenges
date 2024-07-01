print("""A googol ( 10^100 ) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a,b < 100, what is the maximum digital sum?""")

def digit_sum(num):
    snum = str(num)
    total = 0
    for each in snum:
        total += int(each)
    return total

ans = 0
for a in range(2,9):
    temp = a
    for b in range(0,98):
        temp *= a
        ans = max(ans,digit_sum(temp))

for a in range(11, 100):
    temp = a
    for b in range(0,98):
        temp *= a
        ans = max(ans,digit_sum(temp))

print(ans)