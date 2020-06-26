import re
s=input()
pattern=r'[A-Za-z]+ly'
results=re.finditer(pattern,s)
for match in results:
    self_s=match.group()
    print('%s Found at: (%d,%d)' % (self_s ,match.start(), match.end()))