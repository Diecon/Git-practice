#finally - executes the program eventhough an error occured

#Same Zomato example

try:
    items = int(input("Enter the number of items: "))
    total_price = 200 * items
    print("The total price is", total_price)
    average_price = total_price / items  # if user entered 0 it doesn't throw ZeroDivisionError
    print("The average price is", average_price)
except FileNotFoundError:   #intentionally changed to FileNotFoundError to cause error in order to check finally
    print("Item cannot be zero")

finally:
    print("Oops, please try again later")  #the statement inside finally runs even any exception error found

print("System closed") #this or any other upcoming lines of code won't execute/run since its under exception error but "finally works"




