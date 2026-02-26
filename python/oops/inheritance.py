# # inheritance or is a relation : used to aquire the properties and behavours of one class to another class
# # there are 5 types of inheritance
# # 1.single
# # 2.multiple


# # inherit from student from employee

# class student:
#     def __init__(self,name,knwl):
#         self.name=name
#         self.knwl=knwl
#     def st_det(self):
#         print(self.name)
#         print(self.knwl)
# class employee(student):
#     def __init__(self, name, knwl,join_date,sal):
#         super().__init__(name, knwl)
#         self.join_date=join_date
#         self.sal=sal
#     def emp_det(self):
#         super().st_det()
#         print(self.join_date)
#         print(self.sal)
# e=employee("kurumurthy",1,"19-9-2020",50000)
# e.emp_det()

         

# class college:
#     def __init__(self,cname,cid):
#         self.cname=cname
#         self.cid=cid
#     def c_method(self):
#         print(self.cname)
#         print(self.cid)
# class student(college):
#     def __init__(self, cname, cid,sname,branch):
#         super().__init__(cname, cid)
#         self.sname=sname
#         self.branch=branch
#     def s_method(self):
#         super().c_method()
#         print(self.sname)
#         print(self.branch)
# o1=student("MRITS","S1","MK","CSE-DS")
# o1.s_method()
        

# class iphone10:
#     def __init__(self,cam10,p10):
#         self.cam10=cam10
#         self.p10=p10
#     def i10_details(self):
#         print("IPHONE 10")
#         print(self.cam10)
#         print(self.p10)
# class iphone11(iphone10):
#     def __init__(self, cam10, p10,cam11,p11):
#         super().__init__(cam10, p10)
#         self.cam11=cam11
#         self.p11=p11
#     def i11_details(self):
#         super().i10_details()
#         print("IPHONE 11")
#         print(self.cam11)
#         print(self.p11)
# class iphone12(iphone11):
#     def __init__(self, cam10, p10, cam11, p11,cam12,p12):
#         super().__init__(cam10, p10, cam11, p11)
#         self.cam12=cam12
#         self.p12=p12
#     def i12_details(self):
#         super().i11_details()
#         print("IPHONE 12")
#         print(self.cam12)
#         print(self.p12)
# class iphone13(iphone12):
#     def __init__(self, cam10, p10, cam11, p11, cam12, p12,cam13,p13):
#         super().__init__(cam10, p10, cam11, p11, cam12, p12)
#         self.cam13=cam13
#         self.p13=p13
#     def i13_details(self):
#         super().i12_details()
#         print("IPHONE 13")
#         print(self.cam13)
#         print(self.p13)
# io=iphone13(10,"m1",11,"m2",12,"m3",13,"m4")
# io.i13_details()
        

class customer:
    def __init__(self,name,mob):
        self.name=name
        self.mob=mob
    def c_method(self):
        print(self.name)
        print(self.mob)
class bank(customer):
    def __init__(self, name, mob,balance,val_pin):
        super().__init__(name, mob)
        super().c_method()
        self.balance=balance
        self.val_pin=val_pin
    def credit(self,amount,pin):
        
        if pin==self.val_pin and amount>0:
            self.balance+=amount
            print("credit success")
            print("Total balance")
            print(self.balance)
        else:
            print("Invalid pin or amount")
    def debit(self,amount,pin):
        if pin==self.val_pin and amount>0 and amount<self.balance:
            self.balance-=amount
            print("debit success")
            print("Total balance")
            print(self.balance)
        else:
            print("Invalid pin or amount")

ob=bank("MK",7989020757,5000,1909)
ob.credit(500,1909)
ob.debit(50000,1909)




        