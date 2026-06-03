class grandpa:
    def house(self):
        print("white coloured house")

class dad:
    def company(self):
        print("chennai communication")

    def house(self):
        print("green coloured house")  #method overriding in polymorphism

g = grandpa()  #object named g created for grandpa class
d = dad()      #object named d created for dad class
g.house()
d.company()
d.house()      #prints last changed version as output (override)