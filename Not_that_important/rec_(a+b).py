import sys
sys.setrecursionlimit(1500)
def a_plus_b(a,b):
    if b<0:
        coef=-1
    else :
        coef=1
    res=0
    if b==0:
        return a
    res=a_plus_b(a,b-1*coef)+1*coef
    return res



a, b = [int(x) for x in input().split()]
print(a_plus_b(a,b))
