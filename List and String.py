print("\tDisplay Enter User Data in the List.")
Student_1 = []
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
profession = input("Enter Your Profession: ")
Student_1.append(name)
Student_1.append(age)
Student_1.append(profession)
print(Student_1)

print("\tDisplay What we can do Change String and List after get the value.")
Student_1[2]="AI Engineering"
print(Student_1)
Student_1[1]="23"
print(Student_1)
Student_1[0]="Ammar"
print(Student_1)
print(Student_1[5])