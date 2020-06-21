n=int(input())
allowed=0
x = list(map(int, input().split()))
h=int(input())
for i in x:
    if i>=h :
        allowed+=1
print(allowed)
