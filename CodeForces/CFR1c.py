#CodeForce Round 1c Ancient Berland Circus
from math import sqrt, acos, pi, sin

def find_side(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

def find_angle(a,b,c):
    return acos((b*b+c*c-a*a)/(2*b*c))

def find_gcd(A,B):
    if (A < B):
        return find_gcd(B,A)
    if (abs(B)< 0.001):
        return A
    return find_gcd(B, A - (A//B)*B)


points = []
for i in range(3):
    x,y = map(float,input("Please give input (cordinate of points) for 1c :Ancient Berland Circus\n").split())
    points.append([x,y])

a = find_side(points[0], points[1])
b = find_side(points[1], points[2])
c = find_side(points[2], points[0])

p = (a+b+c)/2
s = sqrt(p*(p-a)*(p-b)*(p-c))
r = (a*b*c/(4*s))

A = find_angle(a,b,c)
B = find_angle(b,c,a)
C = find_angle(c,a,b)

x = 2 * find_gcd(A, find_gcd(B,C))

n = round(2*pi/x)

s = 0.5 *n*r*r*sin(2*pi/n)

print("%.6f" %s)