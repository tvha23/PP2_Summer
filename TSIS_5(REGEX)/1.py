import re
s=input()

pattern=r'[^a-zA-Z0-9]'#check if not necessary condition 
result =re.findall(pattern,s)#create list of all results 

if len(result)==0:#if there's found no opposite pattern print yes else no
    print ("YES")
else: print("NO")
'''
for r in result:
    print (result)
'''