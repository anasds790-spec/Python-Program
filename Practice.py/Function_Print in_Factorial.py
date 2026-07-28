print("\tDisplay a Factorial in a Number to use a Function.")

Factorial_Number = int(input("Enter a Number to give a Factorial: "))

def Calc_Factorial(Factorial_Number):
    F = 1
    for H in range(1, Factorial_Number + 1):
        F = F * H  # Accumulate the product
    print(f"The factorial of {Factorial_Number} is: {F}")

# Call the function outside the def block
Calc_Factorial(Factorial_Number)