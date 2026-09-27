print("Display Natural Numbers in ascending Order using Recursion:")
def Print_Numbers(Natural):
    if Natural ==0:#Base Case
        return
    Print_Numbers(Natural-1)
    print(Natural)

Print_Numbers(5)