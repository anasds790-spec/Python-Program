print("Display a Fibonacci Nth Number to use a Recursion.\n")

Number =int(input("Enter Your Number to Calculate Nth-Fibonacci Number:"))
def Calc_Nth(Number):
    if Number ==0:
        return 0
    if Number ==1:
        return 1
    return Calc_Nth(Number-1)+Calc_Nth(Number-2)
Fibonacci =Calc_Nth(Number)
print(Fibonacci)