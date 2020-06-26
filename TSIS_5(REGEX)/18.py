import re
s=input()

pattern=r'[0-9]{1,3}'
results =re.findall(pattern,s)

for result in results:
    print (result)