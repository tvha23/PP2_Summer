import re
s=input()
pattern='[; |, |\*|\n]'
results =re.findall(pattern,s)
s=s.split(pattern,s)
print (s)