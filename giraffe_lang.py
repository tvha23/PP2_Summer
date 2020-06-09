def to_giraffe(a):
    translation=""
    for i in a:
        #if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        if i in "AEOIUaouie":
            translation+='g'
        else:
            translation+=i
    return translation

#a=input()
#print(to_giraffe(a))
print(to_giraffe(input()))