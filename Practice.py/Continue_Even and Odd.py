print("\tDisplay Even Numbers to use a While_Loop for Continue Statement.")
G=0
while G<=20:
    if(G%2!=0):
        G+=1
        continue
    print(G)
    G+=1
print("While-Loop ended Successfuly!")

print("\tDisplay Odd Numbers to use a While_Loop for Continue Statement.")   
L=0
while L<=20:
    if(L%2==0):
        L+=1
        continue
    print(L)
    L+=1
print("\tWhile-Loop ended Successfuly!")