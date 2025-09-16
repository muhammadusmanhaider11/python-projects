#guess game
import random
def guess(x):
    random_no=random.randint(1,x)
    guess=0
    i=0
    while guess != random_no:
        
        i=i+1
        if i==5: # available guesses
            return 0
        guess = int(input(f"guess no between 1 and {x}:"))
        if guess < random_no:
            print('guess again too low')
        elif guess > random_no:
            print('guess again too high')
    print(f'you won the no {random_no} is correct !❤️')
guess(10)