from math import sqrt

target = 36000000
target //= 10

def find_factor_sum(n):
    factors = []
    for i in range(1, int(sqrt(n))+1):
        if not n % i:
            factors.append(i)
            n_i = n//i
            if i != n_i:
                factors.append(n_i)
    return sum(factors)
 
# print(find_factor_sum(1250000))

for k in range(500000,1500000):
    if find_factor_sum(k) >= target:
        print(k)
        break