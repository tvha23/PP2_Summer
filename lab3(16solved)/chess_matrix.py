m, n = [int(x) for x in input().split()]
A=[]
A = [ [ 0 for i in range(n) ] for j in range(m) ] 
for i in range(m):
    if i%2==0:
        q=1
    else :
        q=0
    for j in range (n):
        #print(q)
        A[i][j]=q%2
        q+=1
    

for i in A:#rows in matrix
    for j in i:#elements in row 
        print(j, end='')
    print()