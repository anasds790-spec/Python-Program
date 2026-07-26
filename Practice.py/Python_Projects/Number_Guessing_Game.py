import random

print("\tDisplay a Number Guessing Game to use a While_Loop in a Python.")

Number_to_Guess =random.randint(1,100)

attempts = 0
Score = 100
Penality = 10

while True:
    try:
        Guess =int(input("Guess the Number between 1 and 100: "))
        attempts +=1
        if Guess > Number_to_Guess:
            Score -=Penality
            print("\tToo High!")
        elif Guess < Number_to_Guess:
            Score -=Penality
            print("\tToo Low")
        else:
            print("\tCongratulations! You Guess out the Number.")   
            Final_Score =max(0,Score)
            print(f"\tYour Final_Score is: {Final_Score}") 
            print(f"\tTotal_attempts: {attempts}")
            break
        if(Score <= 0):
            print("\tGame Over! Your Score is 0.")
            print(f"\tGuess Number is: {Number_to_Guess}")
            break
    except ValueError:
        print("Invalid Choice! Please enter a valid Number.")