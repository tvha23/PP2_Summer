x = list(map(int, input().split()))
rec_x1=x[0]
rec_y1=x[1]
rec_x2=x[2]
rec_y2=x[3]
coin_x=x[4]
coin_y=x[5]
#rec_x1>rec_x2 always
if rec_x1<rec_x2:
    temp = rec_x1
    rec_x1=rec_x2
    rec_x2=temp
if rec_y1<rec_y2:
    temp = rec_y1
    rec_y1=rec_y2
    rec_y2=temp
if coin_x>=rec_x2 and coin_x <= rec_x1 and coin_y<=rec_y1 and coin_y>=rec_y2:
    print ("yes")
else: print("no")