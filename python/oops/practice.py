#  class , objects , inheritance--> aquiring properties of parent class

# class parent:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def details(self):
#         print(self.num1)
#         print(self.num2)
# class child(parent):
#     def __init__(self, num1, num2,num3):
#         super().__init__(num1, num2,)
#         # self.num1=num1
#         # self.num2=num2
#         self.num3=num3
#     def getdata(self):
#         super().details()
#         print(self.num3)

# ch=child(10,20,30)
# ch.getdata()

# multi-level inheritance

# class thatha:
#     def __init__(self,age):
#         self.age=age
#     def detail1(self):
#         print("Thatha age:",self.age)

# class nanna(thatha):
#     def __init__(self, age):
#         super().__init__(age)
#     def detail2(self):
#         super().detail1()
#         self.age=self.age-20
#         print("Nanna age:",self.age)
# class child(nanna):
#     def __init__(self, age):
#         super().__init__(age)
#     def detail3(self):
#         super().detail2()
#         self.age=self.age-20
#         print("child age:",self.age)

# obj=child(60)
# obj.detail3()


#  multiple , heirarical , hybrid
  



    
        

        

    
        

        
        

