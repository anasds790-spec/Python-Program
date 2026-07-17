print("\tDisplay nested Dictionary Structure in Python.","\n")
Student = {
  "Name":"Kiara Advani",
  "Age":"21",
 "Subject":{
     "English":"75",
     "Physics":"80",
     "Math":"95",
 },
  "Program":["Data_Science","Machine_Learning","AI_Scientist"]
}
print(Student,"\n")
print("\tDisplay Only Subjects on the Student in Python.","\n")
print(Student["Subject"])
print("\tDisplay Only One Subjects marks on the Student in Python.","\n")
print(Student["Subject"]["Math"])