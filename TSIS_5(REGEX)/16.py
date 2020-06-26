import re
s=input()
n=int(len(s))
while True:#if at the beginnin zeros, delete them :
    i=0
    if s[i]=='0':
        s=s.replace('0','',1)
        i+=1
    else:break
#if there's '.' followed by '0'(s) delete all of them and only leave '.'
s=re.sub(r'\.[0]+','.',s)
print(s)