with open("Practice.txt","r") as f:
    data =f.read()

new_data =data.replace("Java","Python")
print(new_data)

with open("Practice.txt","w") as f:
    f.write(new_data)

print("Display a Word of Learning in a Paragraph.")
word ="Learning"
with open("Practice.txt","r") as f:
    data =f.read()   
    if word in data:
        print("Found")
    else:
        print("Not_Found")   