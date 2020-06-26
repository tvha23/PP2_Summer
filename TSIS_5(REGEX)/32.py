import re
s=input()

pattern=r'[\s,.]+'
s =re.sub(pattern,':',s,2)
print(s)