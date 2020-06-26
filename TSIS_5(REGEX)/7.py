import re
s=input()
pattern=r'[a-z]+_[a-z]+'
results=re.findall(pattern,s)
for result in results:
    print(result)