"""
s=input()
t=input()
ns=dict()
nt=dict()
for i in "qwertyuiopasdfghjklmnbvcxz":
    ns[i]=0
    nt[i]=0
for i in range(0,len(s)):
    ns[(s[i])]+=1
    nt[(s[i])]+=1
for i in ns:
    if ns[i]==nt[i]:
        print (1)
        """
s=input()
t=input()
sorted_s=sorted(s)
sorted_t=sorted(t)
if sorted_s==sorted_t:
    print('Yes')
else:
    print('No')