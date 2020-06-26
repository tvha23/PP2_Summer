import re
s=input()
s=s.strip()
string_list=list(s)
n=len(s)
for i in range(n):
    if s[i]==" ":
        string_list[i]="_"
    if s[i]=="_":
        string_list[i]=" "
print(''.join(string_list))