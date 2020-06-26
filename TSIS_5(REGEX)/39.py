import re
s=input()
pattern=r'\s{2,}'
s=re.sub(pattern,' ',s)
print(s)