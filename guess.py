import random
def guess_the_number():
    number=random.choice(list(range(1,100)) ) #random number we have to guess
    chances=random.choice(list(range(2,11))) #randomly initializing the chances from 2-10.
    print("You have %d chances to Guess"%(chances),"\n")
    while chances:
        guess=int(input("Guess the number: "))
        if number==guess:print("Congo! You had the correct guess");break
        elif chances==1:print("Better Luck Next time :)");break
        else:
            diff=abs(number-guess)
            if diff<10:print("\nAmazing! you are almost close")
            if number>guess:
                print("Hint: Try a higher number" )
            else:print("Hint: Try a lower number")
        chances-=1
        print("Don't worry you still have %d turns\n"%(chances))
    print("The Number was %d, Better Luck Next time :)"%number)
print("Heyaaa! come lets play the guess game")
guess_the_number()
