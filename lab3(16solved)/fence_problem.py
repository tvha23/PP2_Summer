x,y=input().split()
results=list()
a=list()
result=0
can_climb=bool
for i in range(int(x)):
    a=input().split()
    result=int(a[0])+int(a[1])+int(a[2])
    results.append(result)
for re in results:
    if re/3<=int(y):
        can_climb=False
    if re/3>=int(y):
        can_climb=True
        break
if  can_climb:
    print("YES")
else: print ("NO")