def is_Palindrome (a) :
    x=len(a)
    is_p=True
    while x>1:
        if a[0]==a[-1]:
            new_a=a[1:int(len(a)-1)]
            a=new_a
            is_p=True
            x-=2
        else:
            is_p=False
            break
    return is_p

n=int(input())
l=list()
while n>0:
    l.append(input())
    n=n-1
for i in l:
    if is_Palindrome(str(i)):
        print("Yes")
    else: print("No")