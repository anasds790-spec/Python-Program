print("Display a User data in a CSV File.")
import csv
with open("Practice.py/Data.CSV","r")as file:
    csv_reader =csv.reader(file)
    for row in csv_reader:
        print(row)
with open("Practice.py/Data.CSV","a")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["\nAhmad","7","Python","85"])