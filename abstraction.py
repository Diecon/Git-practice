from abc import ABC, abstractmethod

class FeaturePlan(ABC):
    @abstractmethod    #abstract method
    def login(self):
        pass

    @abstractmethod    #abstract method
    def logout(self):
        pass

    def payment(self):  #ordinary method
        pass


class employee(FeaturePlan):
    def login(self):
        print("login credentials")   #throws an error if didnt passed anything inside abstractmethod

    def logout(self):
        print("logout button")


emp = employee()    #object should be only created for child class not "abstract class"(since there is no use in creating one)
emp.login()
emp.logout()
