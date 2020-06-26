import re
s=input()
pattern=r'a.*b$'
results=re.findall(pattern,s)
for result in results:
    print(result)