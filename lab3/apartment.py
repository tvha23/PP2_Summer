a,b,x,y=[int(x) for x in input().split()]
if (x>=a and y>=b) or (y>=a and x>=b):
    if x*y>=a*b:
        print ('Thanks, Nurbek')
else: 
    print('Impossible')
