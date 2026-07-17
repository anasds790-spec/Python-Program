print("\tCreate a Grading System For Students.")
Marks=int(input("Enter Your Final Exam Marks less than 100 or Equal to:"))
if(100>Marks>=90):
    print("According to Your Marks,Your Grade is:A")
elif(90>Marks>=80):
    print("According to Your Marks,Your Grade is:B")  
elif(80>Marks>=70):
    print("According to Your Marks,Your Grade is:C")
elif(Marks<70):
    print("According to Your Marks,Your Grade is:D")       
else:
    print("You are incorrect marks Entered!")    