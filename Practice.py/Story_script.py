print("Display a Story Script Line Number Count in the Story.")
Count =0
with open("Practice.py\Story.txt","r")as f:
    for Line in f:
        print(Line.strip())
        Count +=1

print("Total Number of Lines in Story:",Count)        