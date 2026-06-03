with open("file.txt","r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        if "ERROR" in line:
            print(line.strip())

print("\n")
print("FILES READ USING FOR LOOP - RANGE FUNC")
with open("file.txt","r") as file:
    for _ in range(4):
        print(file.readline().strip())