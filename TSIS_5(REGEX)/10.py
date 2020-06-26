import re
s=input()
s=s.strip()
pattern=r'[\s]'
num_of_spaces=re.findall(pattern,s)
i=0
if len(num_of_spaces)==0:
    print (s)
else:
    while s[i]!=' ':
        print(s[i],end='')
        i+=1
#print (results)
