n=int(input())
res=0
p=3
while n>0:
    bite=int(n%2)
    res+=int(2**p)*bite
    p-=1
    n//=2
    #print(p)
print(res)
"""
  //51447. Bits
    int n,res=0,p=3;;
    cin>>n;
    while(n>0)
    {
        int bite=n%2;
        res+=pow(2,p)*bite;
        p--;
        n//=2;
    }
    cout<<res;

"""
