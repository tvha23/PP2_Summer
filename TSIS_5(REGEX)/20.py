import re
s=input()
'''
You can use re.finditer to iterate over all matches in a string. This gives you (in comparison to re.findall extra
information, such as information about the match location in the string (indexes):
'''
pattern=r'fox'
for match in re.finditer(pattern,s):
    s_start=match.start()
    s_end=match.end()
    s_self=match.group()#~.group(0) and returns whole string
    print('%s is found at:(%d,%d)'%(s_self,s_start,s_end))