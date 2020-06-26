import re
s=input()
pattern='[0-9]$'
results=re.findall(pattern,s)
for result in results:
    print(result)