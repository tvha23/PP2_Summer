import re 
A=list()
push_pattern=re.compile(r'push\s')
while True:
    n=input()
    if n=='end':
        print('Black Devil')
        break

    if re.match(push_pattern, n):
        a=re.split(r'\s',n)
        #print(a)
        A.append(a[1])
        print('OK')
        a.clear()

    if n=='size':
        print(len(A))

    if n=='pop':
        A.pop()
        print('OK')

    if n=='front':
        print(A[0])

    if n=='back':
        print(A[-1])
    if n=='clear':
        A.clear()
        print('OK')
    if n=='total':
        res=0
        for i in A:
            res+=int(i)
        print(res)
        
    
    
