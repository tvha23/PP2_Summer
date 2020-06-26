import re
s=input()
pattern=r'^[a-zA-Z0-9_]+$'
results=re.findall(pattern,s)
for result in results:
    print(result)