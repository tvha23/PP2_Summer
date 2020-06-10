import re

with open('getting started with redex/text.txt', 'r') as f:
    contents=f.read()

#To create raw string:
raw_string=r"This is string\n"
#print(raw_string)

#neccesary to create patternt to search for
pattern = re.compile(r'abc')
pattern=re.compile(r'ABC')
pattern=re.compile(r'\.')

#finditer() returns an iterator that contains all matches 

#MetaCharacters (Need to be escaped):
#. ^ $ * + ? { } [ ] \ | ( )
pattern=re.compile(r'robertdavis@bogusemail\.com')
pattern=re.compile(r'\d{3}\D\d{3}\D\d{4}')
#[abc] means match a or b or c
pattern=re.compile(r'\d{3}[- .*]\d{3}[- .*]\d{4}')

matches=pattern.finditer(contents)
for match in matches:
    print(match)
#print (contents[0:3])

