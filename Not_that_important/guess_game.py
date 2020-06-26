key_word="spaghetti"
is_false=False
while not(is_false):
    guess=input("Enter your guess \n")
    if guess!=key_word :
        is_False=True
        print("Try again!")
    elif guess==key_word:
        print ("Damn right!\n")
        break
