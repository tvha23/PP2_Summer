import re
s=input()
pattern=r'^24'
results=re.findall(pattern,s)
for result in results:
    print(result)