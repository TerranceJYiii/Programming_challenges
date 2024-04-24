print("""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000""")

def powerself(n):
    return n**n

sum = 0
for i in range(1,1001):
    sum += powerself(i)

print(sum%10000000000)