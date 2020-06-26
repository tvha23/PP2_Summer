import re
s=input()
pattern=r'[A-Z]+[a-z]+'
results=re.findall(pattern,s)
for result in results:
    print(result)