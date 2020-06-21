import math
l=list()
for i in range(0,4):
    l.append(int(input()))
if int(abs(l[2]-l[0]))==int(abs(l[3]-l[1])):
    print("YES")
else: print("NO")

