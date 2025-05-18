# a simple quiz game using python

print("Welcome to my computer quiz!")

playing =input("Do you want to play?")

if playing.lower() != "yes": #makes complete text lowercase 
    quit()
    
print("Okay! Let's play :) ")

score=0

answer =input("What does CPU stand for?")
if(answer.lower()=="central processing unit"):
    print("Correct!")
    score+=1
else:
    print("That's incorrect! The correct answer is 'Central Processing Unit'")

answer =input("What does GPU stand for?")
if(answer.lower()=="graphics processing unit"):
    print("Correct!")
    score+=1
else:
    print("That's incorrect! The correct answer is 'Graphics Processing Unit'")

answer =input("What does RAM stand for?")
if(answer.lower()=="random access memory"):
    print("Correct!")
    score+=1
else:
    print("That's incorrect! The correct answer is 'Random Access Memory'")

answer =input("What does PSU stand for?")
if(answer.lower()=="power supply"):
    print("Correct!")
    score+=1
else:
    print("That's incorrect! The correct answer is 'Power Supply'")
    
print(f"You made it! \nYou got {score} questions correct :)")


