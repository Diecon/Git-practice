class grandpa:
    def house(self):
        print("Apsalom residence")

class dad(grandpa):
    def company(self):
        print("chennai communication")

class son(dad,grandpa):
    def degree(self):
        print("btech")



s=son()
s.company()
s.degree()
s.house()