print("\tDisplay a Tuple element find a Value of X by using a While_Loop. ")
Numbers=(1,4,9,16,25,36,49,64,81,100)
X=49
index = 0
while index<len(Numbers):
    if(Numbers[index] == X):
        print("I Found a Value of X is:",index)
    else:
        print("Sorry! We are not Find Out the Value of X.")    
    index+=1
print("\tWhile-Loop Ended Successfuly!")        