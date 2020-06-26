def add(a, b):
    return int(a)+int(b)
def subtract(a,b):
    return int(a)-int(b)
def multiply(a,b):
    return int(a)*int(b)
def divide (a,b):
    return int(a)/int(b)

print("Enter two integers")
a=input()
b=input()
print("Type number of operation you want to use:\n1) Addition")
print("2) Substraction \n3) Multiplication\n4) Division")
x=input()
if x=='1':
    res=int(add(a,b))
    print(1)
elif x=='2':
    res=int(subtract(a,b))
elif x=='3':
    res=int(multiply(a,b))
elif x=='4':
    res=int(divide(a,b))

print(res)





