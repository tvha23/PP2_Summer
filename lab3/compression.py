s=str(input())
s1=""
for i in s:
    if s1.count(i)==0:
        s1+=i
print(s1)
