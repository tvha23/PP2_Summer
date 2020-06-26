import re
s=input()
pattern=r'[0-9]+'
results =re.findall(pattern,s)
num_of_occurence=len(re.findall(pattern,s))
results =re.finditer(pattern,s)
for match in results:
    s_start=match.start()
    s_end=match.end()
    s_self=match.group()
    print ('number "%d" is found at the (%d,%d).'%(int(s_self),s_start,s_end))
    