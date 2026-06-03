class parent:
    def __init__(self):
        self.public_var = "i am public"
        self._protected_var = "i am protected"
        self.__private_var = "i am private"

    def access_from_same_class(self):
        print("public:",self.public_var)
        print("protected:",self._protected_var)
        print("private:",self.__private_var)

class child(parent):
    def access_from_child_class(self):
        print("public:",self.public_var)
        print("protected:",self._protected_var)
        try:
            print("private:",self.__private_var)
        except AttributeError:
            print("throws an error")

class stranger:
    def access_from_stranger_class(self,obj):
        print("public:",obj.public_var)
        print("protected:",obj._protected_var)
        try:
            print("private:",obj.__private_var)
        except AttributeError:
            print("throws an error")


p = parent()
c = child()
s = stranger()

print("\nAccess from same class")
p.access_from_same_class()

print("\nAccess from child class")
c.access_from_child_class()

print("\nAccess from stranger class")
s.access_from_stranger_class(p)