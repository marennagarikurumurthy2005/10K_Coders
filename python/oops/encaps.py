class laptop:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def details(self):
        print(self.name)
        print(self.__price)
        print(" i5 12gen 16Ram,512ROM ")

    def sale(self,offered):
        self.details()
        if offered>self.__price-10000:
            print(f" Im Ready to sale at {offered} ")
        else:
            print(f"i get loss at this cost {offered}, im ok with {self.__price-10000} ")

ob=laptop("LENOVO",62000)
ob.sale(55000)


class mobile:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def details(self):
        print(self.name)
        print(self.__price)
        print("SnapDragon880 16Ram,512ROM ")

    def sale(self,offered):
        self.details()
        if offered>self.__price-10000:
            print(f" Im Ready to sale at {offered} ")
        else:
            print(f"i get loss at this cost {offered}, im ok with {self.__price-10000} ")

m=mobile("REDMI NOTE 14 pro 5G",38000)
m.sale(20000)


        