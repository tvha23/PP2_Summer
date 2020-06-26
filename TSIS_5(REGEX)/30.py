import re
s=input()

pattern=r'Road'
s =re.sub(pattern,'Rd.',s)
print(s)