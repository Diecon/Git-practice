file = open("sample.txt","w")
file.write("hello im am diecon\n")
file.write("how are you\n")
file.close()

file = open("sample.txt","r")
content = file.read()
print("contents in sample.txt are:\n",content)
file.close()

file = open("sample.txt","a")
file.write("my last name is disilva\n")
file.close()

file = open("sample.txt","r")
content = file.read()
print("contents in sample.txt are:\n",content)
file.close()

#with

with open("sample.txt","r") as file:
    print("contents read using with:\n")
    for line in file:
        print(line.strip())