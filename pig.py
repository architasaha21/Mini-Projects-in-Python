"""Pig is a simple die game where players take turns to roll a single die as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a dice-1.
The game ends when total score is 50."""


import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

value=roll()
print(value)


while True:
    players=input("Enter the number of players (2-4) : ")
    
    if players.isdigit():
        players=int(players) #converts string to integer
        if 2<=players<=4:
            break
            
        else:
            print("Invalid Input. Must be between 2-4 players.") 
            continue
    else:
       print("Invalid Input. Please enter a number.") 
       continue
   
print("Number of players selected : ",players)

max_score=50
players_scores=[0]*players
#it puts a zero in list initially for every player