n=int(input())
bob_takes=1#at first bob takes 1
while True:
    n-=bob_takes
    if(n<=0):
        print("Bob")
        quit()
    n-=2*bob_takes#after bob nelson takes 2x 
    if(n<=0):
        print("Nelson")
        quit()
    bob_takes+=1#at the next round he takes one more
    

            
