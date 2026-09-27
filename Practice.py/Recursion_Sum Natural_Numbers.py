print("Display a Sum of Natural Numbers to use a Recursion.")
Natural =int(input("Enter Your Number to Calculate a Sum of Natural Number:"))
def Sum_Numbers(Natural):
    if Natural ==0:
        return 0
    return Sum_Numbers(Natural-1)+Natural
Sum_Numbers(Natural)
Add=Sum_Numbers(Natural)
print(Add)