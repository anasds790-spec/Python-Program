print("\tDisplay a Number of x in a Tuple using For_Loop.")
tuple=(1,4,9,16,25,36,49,64,81,100)
X=81
index=0
for value in tuple:
    if(value==X):
        print("Your tuple value is:",index)
        break
    index+=1
else:
    print("\tFor-Loop ended Successfuly!")