print("\tDisplay a User Number Convert into Factorial by using For_Loop.")
Number=int(input("Enter Your Number by giving a Factorial:"))
Fact = 1
for value in range(1,Number+1):
    Fact *=value
print("Your Number Factorial is:",Fact)