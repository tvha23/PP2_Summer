s=input()
x=len(s)
is_p=True
while x>1:
    if s[0]==s[-1]:
        new_s=s[1:int(len(s)-1)]
        s=new_s
        is_p=True
        x-=2
    else:
        is_p=False
        break
if is_p:
    print("YES")
else:
    print("NO")