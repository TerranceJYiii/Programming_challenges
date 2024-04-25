#CodeForce Round 3c Tic-tac-toe

def check_winning(grid):
    for i in (0,1,2):
        if grid[i] == ".":
            continue
        if grid[i] == grid[i+3] and grid[i] == grid[i+6]:
            return grid[i]
    for i in (0,3,6):
        if grid[i] == ".":
            continue
        if grid[i] == grid[i+1] and grid[i] == grid[i+2]:
            return grid[i]
    if grid[0] == grid[4] and grid[0] == grid[9] and grid[0] != ".":
        return grid[0]
    if grid[2] == grid[4] and grid[2] == grid[6] and grid[2] != ".":
        return grid[2]
    return "."
    
         

grid = ""
for i in range(3):
    grid += input()
dot = grid.count(".")
nx = grid.count("X")
no = grid.count("0")

if abs(nx - no) > 1:
    print("illegal")
else:
    winner = check_winning(grid)
    if winner == "x":
        if nx > no:
            print("the first player won") #---
        else:
            print("the second player won")
    elif winner == "0":
        if no > nx:
            print("the first win") #---
        else:
            print("the second win")
    else:
        if nx == no:
            print("first")
        elif dot == 0:
            print("second")
        else:
            print("draw")