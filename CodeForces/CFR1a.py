#CodeForce Round 1a Theatre Square

def round_full(x,y):
    if x%y == 0:
        return x//y
    else:
        return (x//y)+1
    
m,n,a = map(int,input("Please give input for 1a :Theatre Square\n").split())
print(str(round_full(m,a) * round_full(n,a)))