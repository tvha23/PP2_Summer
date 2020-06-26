import re
s=input()

pattern=input("Enter substring:")
results =re.findall(pattern,s)

print ('"%s" is found %d times.'%(pattern,len(results)))