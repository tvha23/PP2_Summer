import re
s=input()

pattern=r'[\s,.]+'
s =re.sub(pattern,':',s)
print(s)