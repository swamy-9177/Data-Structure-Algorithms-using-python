def issafe(board,i,j,n):
    for col in range(j):
        if board[i][col]=="q":
            return False
    for rows in range(i):
        if board[row][j]=="q":
            return False
    while i>=0 and j>=0 and j<n:
        if board[i][j]=="q":
            return False
        i-=1
        j-=1
    while i>=0 and i<n and j>=0 and j<n:
            if board[i][j]=="q":
                return False

def play(board,row,col,n):
    if row==n:
        for i in board:
            print(i)
        exit()
    for i in range(col):
        if issafe(board,row,i,n):
            board[row][i]="q"
            play(board,row+1,col,n)
            board[row][i]
n=int(input())
board=[[0]*n for i in range(n)]
play(board,0,n,n)