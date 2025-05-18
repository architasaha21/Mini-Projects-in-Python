import random
import string

def generate_password(min_length, numbers=True,special_characters=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special=string.punctuation
    
    characters=letters
    
    if numbers:
        characters += digits
        
    if special_characters:
        characters += special
        
    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False
    
    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(characters) #picks random element from our string character which contains everything
        pwd += new_char
        
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
            
        meets_criteria=True
        if numbers:
            meets_criteria=has_number#if it has number then it will be true else false
            
        if special_characters:
            meets_criteria=meets_criteria and has_special#if it  already is true for number AND has special character then it will be true else false
            
    return pwd



min_length=int(input("Enter the minimum length of password : "))
has_number=input("Do you want to have numbers in the password? (y/n) : ").lower() =='y'
has_special=input("Do you want to have special characters in the password? (y/n) : ").lower()=='y'
password=generate_password(min_length,has_number,has_special)
print("Generating Password....")
print(" Your Password is ",password)