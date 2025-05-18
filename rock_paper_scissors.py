import random

user_wins = 0
comp_wins=0
count=0

print("Welcome to this Rock Paper Scissors Game! \nThe Rules are simple. Type 'r' for Rock, 'p; for Paper and 's' for Scissors or 'q' to quit\n Lets Begin\n\n")

# List of valid options
options = {"r": "Rock", "p": "Paper", "s": "Scissors"}


while count<5:
    
    user=input("Enter your choice : ").lower()
    
    if user=="q":
        break
        
    if user not in options:
        print("Please type in correct input: ")
        continue
    
    # Computer's random choice
    comp = random.choice(list(options.keys()))
        
    print(f"You chose {options[user]}, Computer chose {options[comp]}.")
    
    if user==comp:
        print("It's a Draw")
        
    elif (user == "r" and comp == "s") or (user == "p" and comp == "r") or (user == "s" and comp == "p"):
        print("You won this round!")
        user_wins += 1
        
    else:
        print("You lost this round!")
        comp_wins += 1
    
    count+=1
    
# Final score display
print("Game Over!")
print(f"Final Score -> You: {user_wins}, Computer: {comp_wins}")
print("Thanks for playing!")
    