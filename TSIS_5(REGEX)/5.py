import re
s=input()
pattern=r'^a{1}b{3}$'
result=re.search(pattern,s)
if result:
    print("YES")
else:print("NO")