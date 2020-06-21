n=int(input())
x=list()
if n==0:
    print('0')    
    quit()
while n:
    a=n%7
    x.append(a)
    n//=7
    #print(a,x,n)
x=reversed(x)
print (*x,sep='')# '*' is unpacking thing 

