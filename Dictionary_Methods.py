print("\tDisplay Dictionary Methods in Python.","\n")
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
print("\tDisplay Key Method in Python.")
print(list(Student.keys()))
print("\tDisplay Values Method in Python.")
print(list(Student.values()))
print("\tDisplay items Method in Python.")
Pairs=list(Student.items())
print(Pairs[0:1])
print("\tDisplay get Method in Python.")
print("\tDifference between Keys to value assign and Methods.")
print("keys to assign value.")
print(Student["Name"])
print("get to assign value.")
print(Student.get("Name"))
print("\tDisplay update Method in Python.")
new_dict={
    "City":"Faisalabad",
    "Institute_name":"Virtual University of Pakistan."
}
Student.update(new_dict)
print(Student)