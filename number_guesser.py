#this is a simple number guesser project in python made using api

import random #module


print("Welcome to this Number Guessing Game!")

print("The rules are quite simple. You just have to guess a random number based on the clues given. You are given five tries \nLets start\n\n")

ans=int(input("Enter a random number within (1-20) :"))

# Generate a random number between 1 and 20
num = random.randrange(1, 20)


# Initialize variables
win = False
count = 0  # Keeps track of the number of attempts


while(count<5):
    try:
        ans = int(input("Enter a random number within (1-20): "))
        count += 1  # Increment the attempt count
        
        if(ans==num):
            print(f"Correct! You guessed the number in {count} tries.")
            win = True
            break  # Exit the loop on a correct guess
    
        elif ans > num:
            print("Try again! The number is lower.")
            
        elif ans < num:
            print("Try again! The number is higher.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        
if not win:
    print(f"Aww shucks! All tries are over :(\nThe number was {num}.")
    print("Better luck next time!")
    
    
    






            
        

