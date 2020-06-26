import re
s=input()
pattern=r'([1-2][0-9][0-9][0-9])/([0-1][0-9])/([0-3][0-9])'
results=re.finditer(pattern,s)
s=re.sub(pattern,r'\3/\2/\1',s)
print(s)