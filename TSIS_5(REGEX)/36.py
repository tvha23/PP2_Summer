import re
s=input()
s=s.replace(s[0],s[0].lower(),1)
pattern=r'[A-Z]+'
results=re.findall(pattern,s)
for result in results:
    s =re.sub(pattern,'_'+result.lower(),s,1)
print(s)