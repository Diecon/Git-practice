class grandpa:
    def house(self):
        print("Apsalom residence")

class dad(grandpa):
    def company(self):
        print("chennai communication")

class son(grandpa):
    def degree(self):
        print("btech")



s=son()
s.degree()
s.house()

d=dad()
d.company()
d.house()