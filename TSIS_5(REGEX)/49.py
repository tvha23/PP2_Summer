import re
s=input()
n=int(input())
pattern=r'\b\w{1,len(s)}\b'
results = re.findall(pattern,s)
for result in results:
    if(len(result)>=1 and len(result)<=n):
        print (result)