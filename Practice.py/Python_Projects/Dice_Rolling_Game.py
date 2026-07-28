import random

print("-------\tDice Rolling Game to use a While_Loop in Python.-------")

while True:
    # .lower() converts user input to lowercase ('yes', 'no')
    Choice = input("Please Roll Your Dice (Yes/No): ").lower()

    if Choice == "yes":
        Dice_1 = random.randint(1, 6)
        Dice_2 = random.randint(1, 6)
        print(f"({Dice_1}, {Dice_2})")
    elif Choice == "no":
        print("\tThanks For Playing Game!")
        break  # Stops the loop when they say "no"
    else:
        print("Invalid Choice! Please enter Yes or No for Playing Game.")