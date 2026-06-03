#Zomato example

items = int(input("Enter the number of items: "))
total_price = 200*items
print("The total price is", total_price)
average_price = total_price/items   #if user entered 0 it throws ZeroDivisionError
print("The average price is", average_price)
