print("Display a User task for a to_do list in appends.")
Task =input(("Enter a New Task for a To-do List: "))
with open("Practice.py/to_do.txt","a")as f:
    f.write(Task +"\n")
    print("Task Saved!")