from math import sqrt

target = 36000000
target //= 11

def find_factor_sum(n):
    factors = []
    for i in range(1, int(sqrt(n))+1):
        if not n % i:
            factors.append(i)
            n_i = n//i
            if i != n_i:
                factors.append(n_i)

    sum = 0
    limit = n // 50
    for each in factors:
        if each > limit:
            sum += each
    return sum
 
# print(find_factor_sum(1250000))

for k in range(831500,1500000):
    if find_factor_sum(k) >= target:
        print(k)
        break