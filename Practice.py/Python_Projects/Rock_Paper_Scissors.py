import random

print("-------\tRock, Paper and Scissors Game using a While Loop in Python.-------")
Emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
Guess_One = ("rock","paper","scissors")

def get_user_Choice():
   
   while True:
    Choose = input("\nEnter Your Choice (Rock, Paper, Scissors): ").lower()

    if Choose in Guess_One:
        return Choose
    else:
        print("Invalid Choice! Please enter a valid Choice.")

def Display_Choices(Choose,Computer_Choice):
        
        print(f"Your Choice is: {Choose.capitalize()} {Emojis[Choose]}")
        print(f"Computer Choice is: {Computer_Choice.capitalize()} {Emojis[Computer_Choice]}")

def Determine_Winner(Choose,Computer_Choice):
            
        # All conditions updated to small letters ("rock", "paper", "scissors")
            if Choose == Computer_Choice:
                print("Your Game is Tie! 🤝")
            elif Choose == "rock" and Computer_Choice == "scissors":
                print("\tUser Won the Game! 🎉")
            elif Choose == "paper" and Computer_Choice == "rock":
                print("\tUser Won the Game! 🎉")
            elif Choose == "scissors" and Computer_Choice == "paper":
                print("\tUser Won the Game! 🎉")   
            else:
                # Agar Tie nahi hai aur User nahi jeeta, toh zaroor Computer hi jeeta hoga!
                print("\tComputer Won the Game! 💻")
def Play_Game():
    while True:
        Choose = get_user_Choice()
        Computer_Choice = random.choice(Guess_One)
        
        Display_Choices(Choose, Computer_Choice)
        Determine_Winner(Choose, Computer_Choice)

        Should_Continue = input("Do you want to Continue this Game? (Yes/No): ").lower()
        
        # Agar user "no" bole tabhi break ho, baaki sab par loop chalta rahe
        if Should_Continue == "no":
            print("Thanks for playing! Bye 👋")
            break

# MAIN CALL: Isay BILKUL PEHLE MARGIN (Left side) par likhein!
Play_Game()