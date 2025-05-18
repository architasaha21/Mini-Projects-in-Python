name=input("Type Your Name : ")
print("Welcome",name," to this adventure!")

answer=input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if(answer=="left"):
    answer=input("You come to a river and you can walk around it or swim across it.Which do you choose?Type 'walk' or 'swim' : ").lower()
    
    if(answer=="walk"):
        print("You walked for many miles, ran out of water and died of dehydration. You lose :( ")
    elif(answer=="swim"):
        print("You were swimming across the river and you were eaten by an alligator. You lose :( ")
    else:
        print("Not a valid answer. You lose. Start again.")
        
elif(answer=="right"):
    
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back)")
    
    if(answer=="cross"):
        answer=input("You cross the bridge and meet a stranger. Do you talk to them?(yes/no)")
        
        if(answer=="yes"):
            print("You talked to the stranger and they give you directions to the treasure. You win!")
        elif(answer=="no"):
            print("You ignored the stranger and they are offended and you lose.")
        else:
            print("Not a valid answer. You lose. Start again.")
            
    elif(answer=="back"):
        print("You go back and lose.")
    else:
        print("Not a valid answer. You lose. Start again.")
else:
    print("Not a valid answer. You lose. Start again.")