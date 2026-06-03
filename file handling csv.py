with open("student.csv","w") as f:
    f.write("Name,Age,Class\n")
    f.write("Bob,15,10a\n")
    f.write("James,19,12c\n")
    f.write("Steve,15,10a\n")
    f.write("Dustin,18,12b\n")



#taking input from student.csv, then reading it and writing the file to student_out.csv file
with open("student.csv","r") as inputfile, open("student_out.csv", "w") as outputfile:
    for line in inputfile:
        print(line.strip())
        outputfile.write(line)
