n=input()
mat = [int[input() for i in range (n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()