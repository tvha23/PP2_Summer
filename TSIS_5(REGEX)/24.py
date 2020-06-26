import re
s=input()
pattern=r'([1-2][0-9][0-9][0-9])/([0-1][0-9])/([0-3][0-9])'
results=re.findall(pattern,s)

for result in results:
    print (result)