def tribonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    res=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
    return res
n=int(input())
print(tribonacci(n))    
    