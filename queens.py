n=int(input())
board=[[['0']*n for i in range(n)]for j in range(n)]
if nQueen(board,0):
    printSolution(board)

def nQueen(board,r):
    if r==len(board):
        return True   
    for c in range(len(board)):
        if check(board,r,c):
            board[r][c]='1'
            if nQueen(board,r+1):
                return True
            board[r][c]='0'
def check(board,r,c):
    for i in range(r):
        if board[i][c]=='1':#checks for coloumn
            return False
    i=r
    j=c
    while i>=0 and j>=0:#right diagonal
        if board[i][j]=='1':
            return False
    i=i-1
    j=j-1
    i=r
    j=c
    while i>=0 and j<len(board):#left diagonal
        if board[i][j]=='1':
            return False
    i=i-1
    j=j+1
    return True
def printSolution(board):
    for i in range(n):
        for j in range(n):
            print (board[i][j],end=' ')
        print()
        
        
        
            
            
    
    
    






