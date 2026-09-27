print("Display a Line_No to Find a Word in a Python File.")
def Check_Line_Number():
    word ="Python"
    data =True
    Line_No =1

    with open("Practice.txt") as f:
        while True:
            data =f.readline()
            if(word in data):
             print (Line_No)
             return Line_No
            Line_No +=1
    return-1
Check_Line_Number()