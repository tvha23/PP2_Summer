'''
    int n;
        cin>>n;
    int a[n];
    for(int i = 0 ; i < n ; i++)
        cin>>a[i];

    int count,max;
    int first,last,x;

        cin>>x;

    for(int j = 0 ; j < x ;j++){
        cin>>first>>last;

        max = -9e8;
        count = 0;
        
    for(int i = first ; i <= last ; i++)
        if(max<a[i])
        {
            max = a[i];
            count++;
        } 
    cout<<count<<endl;
    }
'''