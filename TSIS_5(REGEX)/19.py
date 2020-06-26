import re
s=input()

pattern=[r'fox',r'dog',r'horse']
n=int(len(pattern))
for i in range(0,n):
    results =re.findall(pattern[i],s)
    if results:
        #for result in results:
            print ('%s is found %d times'%(pattern[i],len(results)))
    else:print("%s is not find"%pattern[i])
