print("\tDisplay a Sum of First Natural Numbers to use a Recurssion Function.")
def Calculate_Sum(Number):
    if(Number ==0):
        return 0
    return Calculate_Sum(Number-1) +Number

Number =int(input("Enter Your Number by giving a Natural Number Sum is: "))
Sum =Calculate_Sum(Number)
print("Your Sum of Natural Number is: ",Sum)