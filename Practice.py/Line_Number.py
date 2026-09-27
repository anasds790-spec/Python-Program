print("Display a File Content Read and Print Line by Line in Python.")
with open("Practice.py/notes.txt","r")as f:
    data =f.read()
    print(data)