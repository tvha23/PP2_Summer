import re
s=input()
pattern=r'\s{1,}'
s=re.sub(pattern,'',s)
print(s)