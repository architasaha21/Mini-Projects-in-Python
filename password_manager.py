pwd=input("What is the master password?")

def view():
    pass

def add():
    name=input("Account Name : ")
    pwd=input("Password : ")
    with open("passwords.txt", "a") as f: #if it doesn't exist, it creates it. if it exists, it adds to the file.
        f.write(name+" | "+pwd)      
        

while True:
    mode=input("Would you like to add a new password or view the existing ones?(view/add): ").lower()

    if mode=="q":
        break
    
    if mode=="view":
        view()
        
    elif mode=="add":
        add()
    else:
        print("Invalid Mode") 
        continue