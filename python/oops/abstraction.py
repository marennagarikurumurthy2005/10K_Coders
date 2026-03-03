from abc import ABC,abstractmethod
# class RBI(ABC):
#     @abstractmethod
#     def rate(self,roi):
#         pass
#     @abstractmethod
#     def type(self,acctyp):
#         pass

# class SBI(RBI):
#     def rate(self,roi):
#         print(roi)
#     def type(self,acctyp):
#         print(acctyp)
    
#     print("rateofsbi",id(rate))
#     print("typeofsbi",id(type))

# class Canara(RBI):
#     def rate(self,roi):
#         print(roi)
#     def type(self,acctyp):
#         print(acctyp) 

#     print(id(rate))
#     print(id(type))

# class ICICI(RBI):
#     def rate(self,roi):
#         print(roi)
#     def type(self,acctyp):
#         print(acctyp)

# obj1=SBI()
# obj1.rate("10%")
# obj1.type("Savings")
# obj2=Canara()
# obj2.rate("10%")
# obj2.type("Savings")


class College(ABC):
    @abstractmethod
    def details(self,name):
        pass
    @abstractmethod
    def nos(self,strength):
        pass

class cse(College):
    def details(self,name):
        print(name)
    def nos(self,strength):
        print(strength)
class mech(College):
    def details(self,name):
        print(name)
    def nos(self,strength):
        print(strength)
class ece(College):
    def details(self,name):
        print(name)
    def nos(self,strength):
        print(strength)
class civil(College):
    def details(self,name):
        print(name)
    def nos(self,strength):
        print(strength)
obj1=cse()
obj1.details("MRITS-CSE")
obj1.nos(120)

obj2=mech()
obj2.details("MRITS-Mech")
obj2.nos(120)

obj3=ece()
obj3.details("MRITS-ECE")
obj3.nos(120)

obj4=civil()
obj4.details("MRITS-CIVIL")
obj4.nos(120)
