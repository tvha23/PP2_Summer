import math
x, y = map(int, input().split())
gc=math.gcd(x,y)
lc=(x*y)/gc
print(int(gc)+int(lc))
