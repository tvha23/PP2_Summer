number=42069
is_True=False
lives=5
while not(is_True) and lives>=0:
    guess=int(input("Guess a number, a nice one?\n"))
    if number==guess:
        print("damn right!")
        break
    elif number!=guess:
        lives-=1
        is_True=False
        print("Try again!")
        if(lives==-1):
            print("\nYou tried buddy...\nNow, get out of here")

