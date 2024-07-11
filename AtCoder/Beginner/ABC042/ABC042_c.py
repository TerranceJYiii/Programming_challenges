N,K = map(int,input().split())
D = input().split()

def check_condition(n):
    sN = str(n)
    if any(d in sN for d in D):
        return True
    return False

ans = check_condition(N)
while ans:
    N += 1
    ans = check_condition(N)
print(N)
