print("\tCheck Largest Number.")
R=int(input("Enter Your 1st Number Store in R:"))
S=int(input("Enter Your 2nd Number Store in S:"))
T=int(input("Enter Your 3rd Number Store in T:"))
if(R>=S and R>=T):
    print("Your Largest Number is R.")
elif(S>=R and S>=T):
    print("Your Largest Number is S.")
else:
    print("Your Largest Number is T.")    