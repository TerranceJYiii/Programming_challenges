def reflect(s,t): # S = horizontal, t = slender side
    if t > s:
        return reflect(t,s)
    elif s == t:
        return s
    elif s % t == 0: 
        return (2*(s//t)-1) * t
    else:
        return (s//t * t * 2) + reflect(t, s%t)


N,X = map(int,input().split())
print(N + reflect(X, N-X))
