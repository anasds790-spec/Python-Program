print("Display a Calculate Factorial Number to use a Recursion.")
Factorial=int(input(("Enter Your Number to Calculate a Factorial:")))
def Cal_Fact(Factorial):
    if(Factorial ==1 or Factorial ==0):
        return 1
    return Cal_Fact(Factorial-1)*Factorial
Cal_Fact(Factorial)
Calculate =Cal_Fact(Factorial)
print(Calculate)