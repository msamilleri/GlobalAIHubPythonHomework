import  random
name=input("What is Your Name ? = ")
if(name==""):
    print(" You Have a Mistake")
else:
    print("Welcome ",name)
    Game_Dictinary=['python','AI','software','developer']

    right=int(input(" how many times you want try"))
    last_word=''
    guesses=''
    guess_Word=random.choice(Game_Dictinary)
    wordCopm = "*" * len(guess_Word)
    print("Here is your word")
    while right>0:
        mistake=0
        for char in guess_Word:
            if char in guesses:
                print(char)
            else:
                print('*')
                mistake+=1
        if mistake==0:
            print("you win")
            print(" Word is :",guess_Word)
            break
        guess = input("Please guess a letter")
        guesses+=guess
        if guess not in guess_Word:
            print("mistkae you louse one right")
            right-=1
            print("you have just right :",right)
        if right==0:
            print("Losse Game TRY again")












