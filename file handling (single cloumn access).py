import csv
from csv import DictReader

with open("student.csv") as csvfile:
    reader = DictReader(csvfile)
    print("ONLY AGE OF STUDENT.CSV FILE USING DictReader")
    for column in reader:
        print(column["Age"])



#array based method of accessing a single column

print("\n")
with open("student.csv") as csvfile:
    lines = csvfile.readlines()
    print("ONLY AGE OF STUDENT.CSV FILE USING Array method")
    for column in lines[1:]:   #[1:] is used to skip header 
        Age = column.strip().split(",")
        print(Age[1])