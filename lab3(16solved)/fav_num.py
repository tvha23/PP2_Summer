s=input()
last_number=int(s[-1])
res=0
for i in s:
    res+=int(i)
if res%last_number==0:
    print("Yes")
elif res%last_number!=0 : print("No")

    