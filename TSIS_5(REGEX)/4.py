import re
s=input()
pattern=r'^a{1}b?$'
result=re.search(pattern,s)
if result:
    print("YES")
else:print("NO")