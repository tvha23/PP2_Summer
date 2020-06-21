X=0
Y=0
s=input()
for i in s:
    if i=='U':
        Y+=1
    elif i=='D':
        Y-=1
    elif i=='L':
        X-=1
    elif i=="R":
        X+=1
if X==0 and Y==0:
    print ("True")
else: print ("False")