print("\tDisplay a Number Check Even and Odd to use a Function.")
Number_Check =int(input("Enter Your Number Check Even or Odd: "))
def Number(Number_Check):
    #if_elif Condition Use Check Even or Odd.
    if Number_Check %2==0:
        print("Your Number is Even: ",Number_Check)
    elif Number_Check %2!=0:
        print("Your Number is Odd: ",Number_Check)  
    else:
        print("Your Number is Invalid!")      
Number(Number_Check)