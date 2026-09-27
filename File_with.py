print("Display a With Character used read in a Python.")
with open("Python_with.txt","r") as f:
    data =f.read()
    print(data)   

print("Display a With Character used write in a Python.")
with open("Python_with.txt","w+") as f:
   f.write("Book name is Founder.")

print("Display a With Character used Append in a Python.") 
with open("Python_with.txt","a+") as f: 
   f.write("\nBook Writer name is Hitesh Obreo.")