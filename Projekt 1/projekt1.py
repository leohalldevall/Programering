import random
import os

os.system('cls')

print("Välkommen till Gissa Talet. Spelet går ut på att du ska gisa ett tal mellan 1-100 under sju försök")

while True:
    number = random.randint(1, 100)
    tries = 0

    print(number)
    while tries < 7:
        try:
            guess = int(input("guess"))
        except:
            print("Du skrev med bokstäver istället för siffror")
            continue
        

        if guess == number:
            break
   
        elif guess == 0:
            exit()  
        
        elif guess < number:
            tries = tries + 1
            print("För lågt")
        elif guess > number:
            tries = tries + 1
            print("för högt")

    if tries == 7: 
        print("game over")
        print(f"Haha you did not find my secret number. It was {number} feel free to try again or press 0 to exit")
        #exit()#

    else: 
        print(f"you won and it took, {tries+1} tries")




