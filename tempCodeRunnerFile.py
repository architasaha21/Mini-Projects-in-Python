mport os


if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1. Created by Archita")
    x=input("Enter the text you want to convert to speech (or 'q' to quit): ")
    
    # If the user enters 'q', the program will quit
    if x=="q":
        print("Quitting Robo Speaker....")
        exit()
    os.system(f'espeak "{x}"')