import re
email="[^@]+@[a-z]+\.[a-z]+"
n=str(input())
x=n.split('@')
y=n.split('.')

if re.search(email,n) and int(len(x))==2 and int(len(y))==2 :
    print("Yes")
else: print("No")

