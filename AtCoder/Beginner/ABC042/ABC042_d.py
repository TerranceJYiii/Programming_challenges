import numpy as np
H,W,a,b = map(int,input().split())

limit = 10 ** 9 + 7

newH = H - a
box = np.zeros((newH,W))
for i in range(newH):   # row box
    box[i][0] = 1
for j in range(W):      # column box
    box[0][j] = 1

for i in range(1,newH): # row box
    for j in range(1,W):# column box
        box[i][j] = box[i-1][j] + box[i][j-1]
        if box[i][j] > limit:
            box[i][j] = box[i][j] % limit

box2 = np.zeros((a+1,W-b))
box2[0][:] = box[newH-1][b:W]

origin = box2[0][0]
for k in range(1, a + 1):   # row box2
    box2[k][0] = origin

for k in range(1,a+1):
    for l in range(1, W-b):
        box2[k][l] = box2[k-1][l] + box2[k][l-1]
        if box2[k][l] > limit:
            box2[k][l] = box2[k][l] % limit

print(int(box2[-1][-1]))