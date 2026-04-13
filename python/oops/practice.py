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
  

class questions:
    q1="find the min distance of the fib number to the sum of array"
    hint="a<sum<b ; a,b are fib numbers"
    q2="find the time difference of give time interval"
    input="10:10am-10:30pm"
    q3="find the list is in arithmetic or geometric sequence else print -1"
    hint="ap distance between numbers is same , gp ratio of numbers is same"
    q4="insert * between even numbers - between odd numbers do not consider 0 as even"
    example="254809763 to 254*809-763"

    



    
        

        

    
        

        
        

