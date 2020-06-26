import re
s=input()
n=len(s)
pattern=r'\b[\w][\w][\w][\w]+\b'
results =re.findall(pattern,s)
#print(len(results))

for result in results:
    print (result)