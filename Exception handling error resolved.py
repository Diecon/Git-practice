#try - tries to run the program
#throw - throws the error to except
#except (catch in java) - handles the error without crashing the system
#finally - executes the program eventhough an error occured .

#Same Zomato example

try:
    items = int(input("Enter the number of items: "))
    total_price = 200 * items
    print("The total price is", total_price)
    average_price = total_price / items  # if user entered 0 it doesn't throw ZeroDivisionError
    print("The average price is", average_price)
except ZeroDivisionError:
    print("Item cannot be zero")


