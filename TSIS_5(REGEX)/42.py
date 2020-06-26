import re
s=input()
pattern=r'http[s]*?://[a-zA-Z0-9-._~/]+\.+[a-zA-Z0-9]{2,3}/+[a-zA-Z0-9-._~/]+'
results =re.findall(pattern,s)
print(results)
for result in results:
    print (result)