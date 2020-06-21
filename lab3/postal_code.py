x, y = [int(x) for x in input().split()]
s=input()
a=s.split("-")
if len(a)==2:
    if len(a[0])==x:
        if len(a[1])==y:
            print("Yes")
else : print("No")