import re
s=input()

pattern=r''
results =re.findall(pattern,s)

for result in results:
    print (result)