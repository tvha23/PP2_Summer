import re
s=input()
pattern=r'[a-z]'
s=re.sub(pattern,'',s)
print(s)