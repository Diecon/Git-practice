class parent:
    def public_method(self):
        print("im a public method")

    def _protected_method(self):
        print("im a protected method")

    def __private_method(self):
        print("im a private method")

    def access_from_same_class(self):
        self.public_method()
        self._protected_method()
        self.__private_method()

class child(parent):
    def access_from_child_class(self):
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
        except AttributeError:
            print("error occurs for private method")

class stranger:
    def access_from_stranger_class(self,obj):
        obj.public_method()
        obj._protected_method()
        try:
            obj.__private_method()
        except AttributeError:
            print("error occurs for private method")



p = parent()
c = child()
s = stranger()

print("\nAccess from same class:")
p.access_from_same_class()

print("\nAccess from child class:")
c.access_from_child_class()

print("\nAccess from stranger class:")
s.access_from_stranger_class(p)