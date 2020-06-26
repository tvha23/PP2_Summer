import re
s=input()
pattern=r'([a-z])([A-Z])'
s=re.sub(pattern,r"\1 \2",s)
print(s)