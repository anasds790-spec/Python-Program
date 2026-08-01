print("\tDisplay a Forward Number upto 50 to use a Recursion.")
Number =int(input("Enter Your Number between upto 1 and 50: "))
#Recursive Function
def Display(Number):
    if(Number ==51):
        return
    print(Number)
    Display(Number+1)

#Function Call
Display(Number)

#Second Program
print("\tDisplay a Backward Number upto 50 to use a Recursion.")
Number =int(input("Enter Your Number between upto 1 and 50: "))
#Recursive Function
def Display(Number):
    if(Number ==0):
        return
    print(Number)
    Display(Number-1)

#Function Call
Display(Number)