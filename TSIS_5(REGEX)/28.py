import re
s=input()

pattern=r'[a|e]\w+'
results =re.findall(pattern,s)

for result in results:
    print (result)