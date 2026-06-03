feedback = input("Enter your feedback:")
with open("feedback.txt","a") as record:
    record.write(feedback + "\n")

print("Thanks for your feedback")