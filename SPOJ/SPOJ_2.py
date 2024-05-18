# SPOJ 2 : Prime Generator
def SieveOfEratosthenes(m, n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    for p in range(max(2,m), n+1):
        if prime[p]:
            print(p)

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    SieveOfEratosthenes(m,n)