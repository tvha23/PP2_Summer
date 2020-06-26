import re
s=input()
s=s.strip()

pattern=r'[a-zA-Z]+[.|!|?]{1}'
results=re.findall(pattern,s)
if len(results)==0:
#After stripping, add a coma to the sequence to mark last word, if it's not already done :
    s=s+'.'
results=re.findall(pattern,s)
print(results[0][:-1])#print til coma


