print("\tDisplay a User Number Convert into Factorial by using For_Loop.")
Number = int(input("Enter Your Number by giving a Factorial:"))
Fact = 1
S = 1
while (S<=Number):
    Fact *=S
    S+=1
#print("Your Number Factorial is:",Fact)  
print(f"{Fact} X {S} ={Fact*S}")  