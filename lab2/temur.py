m, n = [int(x) for x in input().split()]
A=[]
A = [ [ 0 for i in range(n) ] for j in range(m) ]
for i in range(m):#for the top and left part of the matrix there's only one way to reach 
    for j in range(n):
        if i==0:
            A[i][j]=1
        if j==0:
            A[i][j]=1

for i in range(1,m):#for others, it's sum of ways of top and left of the matrix 
    for j in range(1,n):
        A[i][j]=A[i-1][j]+A[i][j-1]
'''
for i in A:#rows in matrix
    for j in i:#elements in row 
        print(j, end='')
    print()
'''
print(A[m-1][n-1])
        

