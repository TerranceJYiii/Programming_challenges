with open("Task_Day8.txt","r") as infile:
    lines = infile.readlines()

board = [[0]*50,[0]*50,[0]*50,[0]*50,[0]*50,[0]*50]
# board = [[0]*7,[0]*7,[0]*7]

def lit_board(size):
    col,row = map(int,size.split("x"))
    for h in range(row):
        for w in range(col):
            board[h][w] = 1
    # print(f"{col} x {row}")
    # for row in board:
        # print(row)

def shift_row(row, index):
    board[row] = board[row][-index:] + board[row][:-index]
    
def shift_col(col,index):
    temp = [board[i][col] for i in range(6)]
    temp = temp[-index:] + temp[:-index]
    for i in range(6):
        board[i][col] = temp[i]


for line in lines:
    ins = line.split()
    if ins[0] == "rect":
        lit_board(ins[1])
    else:
        if ins[1] == "row":
            row = int(ins[2].split("=")[1])
            index = int(ins[-1])
            shift_row(row,index)
        else:
            col = int(ins[2].split("=")[1])
            index = int(ins[-1])
            shift_col(col,index)
    # for each in board:
        # print(each)
    # print()

ans = 0
for each in board:
    print(each)
    ans += each.count(1)
print(ans)
