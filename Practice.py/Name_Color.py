print("Display information to user Name and Color in Python.")
Name =input("Enter Your Name: ")
Favourite_Color =input("Enter Your Favourite Color: ")
with open("User_info.txt","w") as f:
    f.write(Name +"\n")
    f.write(Favourite_Color)