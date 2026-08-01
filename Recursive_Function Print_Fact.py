print("\tDisplay a Factorial Number by User to use a Recurssive Function.")
def Factorial(Number):
    # Handle negative numbers
    if Number < 0:
        return "Factorial does not exist for negative numbers!"
    # Base cases
    if Number == 1 or Number == 0:
        return 1
    # Recursive case
    return Factorial(Number - 1) * Number

# Take input
Number= int(input("Enter a Number to find its Factorial: "))

# Function Call & Print Result
Result =Factorial(Number)
print("Your Number Factorial is:", Result)