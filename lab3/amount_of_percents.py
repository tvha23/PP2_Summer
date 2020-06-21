#Learn to take input with spaces and newlines
x = list(map(int, input().split()))
odd=0
even=0
for i in x:
    if(i>=0):
        if i%2==1:
            odd+=1
        if i%2==0:
            even+=1
oddperc=float(odd/(odd+even)*100)
evenperc=float(100-oddperc)
if evenperc-int(evenperc)==0:
    evenperc =int(evenperc)
if oddperc - int(oddperc)== 0:
    oddperc=int(oddperc)
if type(oddperc)==float and type(evenperc)==float:
    print( str( '{0:.6}'.format(evenperc) )+"% "+str('{0:.6}'.format(oddperc))+"%")
else :    print( str( evenperc )+"% "+str(oddperc)+"%")
 
