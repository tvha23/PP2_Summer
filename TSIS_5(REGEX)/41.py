import re
s=input()
pattern=r'[^a-zA-Z0-9]'
s=re.sub(pattern,'',s)
print(s)