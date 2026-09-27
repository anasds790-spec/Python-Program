print("Display a Numbers Containing in even Separated by Comma in File.")
Count =0
with open("Practice.py\Comma_Even.txt") as f:
    data=f.read()    

Numbers =data.split(",")    
for Value in Numbers:
    if(int(Value) %2==0):
        Count +=1

print(Count)        