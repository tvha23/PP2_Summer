import re
s=input()

pattern=r'\b\w{5}\b'
results =re.findall(pattern,s)

for result in results:
    print (result)