x, y = map(int, input().split())
for i in range(x,y+1):
    if i%7==1 or i%7==2 or i%7==5:
        print(i,end=' ')