n=int(3)
m=int(input())
A=[]
for i in range(m):
    a=input().split()
    A.append(a)
for row in range(m-1):
    x=0
    if A[row][x]>A[row+1][x]:
        A[row], A[row+1] = A[row+1],A[row] 
print()
for i in A:#rows in matrix
    for j in i:#elements in row 
        print(j, end=' ')
    print()



'''
B=[]
B = [ [ 0 for i in range(m) ] for j in range(n) ] 

for j in range (n):
    for i in range(m):
        B[j][i]=int(A[i][j])

for row in range(n):
    for i in range(len(B[row])-1): 
        for j in range(0, m-i-1): 
            if B[row][j] > B[row][j+1] : 
                B[row][j], B[row][j+1] = B[row][j+1], B[row][j] 

print (B)
'''




