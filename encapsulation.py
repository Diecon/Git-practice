class order:
    def __init__(self, customer_name,items, price, quantity,discount):
        self.customer_name = customer_name
        self.items = items
        self.__price = price
        self.quantity = quantity
        self.__discount = discount

    def __total_price(self):
        return (self.__price * self.quantity) - self.__discount

    def _admin_view(self):
        return {
            'customer_name': self.customer_name,
            'items': self.items,
            'price': f"${self.__price}",
            'total_amount': f"${self.__total_price()}",
            'quantity': self.quantity,
            'discount applied': f"${self.__discount}",
        }

    def customer_view(self):
        return {
            'customer_name': self.customer_name,
            'items': self.items,
            'total_amount': f"${self.__total_price()}",
            'quantity': self.quantity,
        }

order = order("Disilva",['pepsi','cola'],80,2,10)

class admin:
    def show_order(self,order):
        print(order._admin_view())

class customer:
    def show_order(self,order):
        print(order.customer_view())


ad = admin()
cus = customer()

print("\nADMIN VIEW")
ad.show_order(order)

print("\nCUSTOMER VIEW")
cus.show_order(order)