print("\tDisplay a Multiplication Table by Enter User Number in a While_Loop.")
Num=int(input("Enter a Number by giving a table:"))
R=1
while(R<=10):
    print(f"{Num} x {R} = {Num*R}")
    R+=1
print("While-Loop Ended Successfuly!")