n= int(input())#number of columns and rows
a=[]
for i in range(n):          # A for loop for row entries 
    a1 =[] 
    for j in range(n):      # A for loop for column entries 
         a1.append(int(input())) 
    a.append(a1) 
b=[]
for i in range(n):          # A for loop for row entries 
    b1 =[] 
    for j in range(n):      # A for loop for column entries 
         b1.append(int(input())) 
    b.append(b1) 
r = [[0 for row in range(n)] for col in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):  
            r[i][j]+=a[i][k]*b[k][j]
for i in r:
    print(i)