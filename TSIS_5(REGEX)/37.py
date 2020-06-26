import re
s=input()
pattern=r'_[a-z]{1}'
results=re.findall(pattern,s)
for result in results:
    s =re.sub(pattern,result[-1].upper(),s,1)
print(s)