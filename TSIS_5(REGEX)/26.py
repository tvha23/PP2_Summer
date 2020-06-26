import re
s=input("Enter pair of words:")    
pattern=r'P\w+\sP\w+'
results=re.findall(pattern,s)
if results:
    print(results)
else:print("No match")