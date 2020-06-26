import re
s=input()
pattern=r'\w*z+\w*'
results=re.findall(pattern,s)
#if len(results)!=0:
#print(s)
print (results)
for i in results:
    print(i)