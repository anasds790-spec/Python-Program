print("\tDisplay a List of element to use a Recursive Function.")
#Recursion Function.
def City_List(lst,index=0):
    if(index ==len(lst)):
        return
    print(lst[index])
    City_List(lst,index+1)

Cities =["New-York","Islamabad","Karachi","Edinburgh","Dellas"]  
City_List(Cities)  