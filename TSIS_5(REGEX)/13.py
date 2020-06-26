import re
s=input()
#pattern=r'^[^z]\w*z+\w*[^z]$' this will not work for sentences, only for word
pattern=r'\b(?!z)\w*z+\w*(?!z)\B'
'''
(?!...)
Matches if ... doesn’t match next. This is a negative lookahead assertion. 
For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.
'''
#\B at the beginnig of string means won't match if string at the beginning,
# if \B at the end it's opposite
results=re.search(pattern,s)
if results:
    print('YES')
else:print('NO')