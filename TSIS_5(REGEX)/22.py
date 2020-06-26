import re
s=input()

pattern=input("Enter substring:")
num_of_occurence=len(re.findall(pattern,s))
results =re.finditer(pattern,s)
for match in results:
    s_start=match.start()
    s_end=match.end()
    s_self=match.group()
    print ('"%s" is found at the (%d,%d) %d times.'%(pattern,s_start,s_end,num_of_occurence))
    