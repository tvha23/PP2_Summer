print("program to raise Nth power of number M")
def power(a,b):
    res=1
    for i in range(1,b+1):
        res*=a
    return res
a=int(input())
b=int(input())
print(power(a,b))