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
        

# class customer:
#     def __init__(self,name,mob):
#         self.name=name
#         self.mob=mob
#     def c_method(self):
#         print(self.name)
#         print(self.mob)
# class bank(customer):
#     def __init__(self, name, mob,balance,val_pin):
#         super().__init__(name, mob)
#         super().c_method()
#         self.balance=balance
#         self.val_pin=val_pin
#     def credit(self,amount,pin):
        
#         if pin==self.val_pin and amount>0:
#             self.balance+=amount
#             print("credit success")
#             print("Total balance")
#             print(self.balance)
#         else:
#             print("Invalid pin or amount")
#     def debit(self,amount,pin):
#         if pin==self.val_pin and amount>0 and amount<self.balance:
#             self.balance-=amount
#             print("debit success")
#             print("Total balance")
#             print(self.balance)
#         else:
#             print("Invalid pin or amount")

# ob=bank("MK",7989020757,5000,1909)
# ob.credit(500,1909)
# ob.debit(50000,1909)



# class father:
#     def __init__(self,fname):
#         self.fname=fname
#     def f_details(self):
#         print(self.fname)
# class mother:
#     def __init__(self,mname):
#         self.mname=mname
#     def m_details(self):
#         print(self.mname)
# class child(father,mother):
#     def get_details(self,cname):
#         print(cname)
#         self.f_details()
#         self.m_details()
        
    




# class animal:
#     def __init__(self,bc):
#         self.bc=bc
#     def ani_det(self):
#         print(self.bc)
# class dog(animal):
#     def __init__(self, bc,sound,ani):
#         super().__init__(bc)
#         self.sound=sound
#         self.ani=ani
#     def dog_det(self):
#         super().ani_det()
#         print(self.ani)
#         print(self.sound)
# class cat(animal):
#     def __init__(self, bc,sound,ani):
#         super().__init__(bc)
#         self.sound=sound
#         self.ani=ani
#     def cat_det(self):
#         super().ani_det()
#         print(self.ani)
#         print(self.sound)
# class lion(animal):
#     def __init__(self, bc,sound,ani):
#         super().__init__(bc)
#         self.sound=sound
#         self.ani=ani
#     def lion_det(self):
#         super().ani_det()
#         print(self.ani)
#         print(self.sound)

# obj=dog("red","bow","dog")
# obj.dog_det()
# obj2=cat("red","meow","cat")
# obj2.cat_det()
# obj3=lion("red","roar","lion")
# obj3.lion_det()
        
        
# class college:
#     def __init__(self,cname):
#         self.cname=cname
#     def c_details(self):
#         print(self.cname)
# class cse(college):
#     def __init__(self, cname,bname):
#         super().__init__(cname)
#         self.bname=bname
#     def cse_details(self):
#         super().c_details()
#         print(self.bname)
# class ece(college):
#     def __init__(self, cname,bname):
#         super().__init__(cname)
#         self.bname=bname
#     def ece_details(self):
#         super().c_details()
#         print(self.bname)
# class mech(college):
#     def __init__(self, cname,bname):
#         super().__init__(cname)
#         self.bname=bname
#     def mech_details(self):
#         super().c_details()
#         print(self.bname)
# obj1=cse("MRITS","CSE-B1")
# obj1.cse_details()
# obj2=ece("MRITS","ECE-B2")
# obj2.ece_details()
# obj3=mech("MRITS","MECH-B3")
# obj3.mech_details()

        


# class A():
#     def a_details(self):
#         print("Class A")
# class B():
#     def b_details(self):
#         print("Class B")
# class C(A,B):
#     def c_details(self):
#         print("Class C")
# class D(C):
#     def d_details(self):
#         print("Class D")
# d1=D()
# d1.a_details()
# d1.b_details()
# d1.c_details()
# d1.d_details()


# class A:
#     def a_details(self):
#         print("Class A")
# class B(A):
#     def b_details(self):
#         print("Class B")
# class C(B):
#     def c_details(self):
#         print("Class C")
# class D(B):
#     def d_details(self):
#         print("Class D")

# class E(B):
#     def e_details(self):
#         print("E Class")
# class F(D,C,E):
#     def f_details(self):
#         print("F class")

# # class G(D):
# #     def g_details(self):
# #         print("G class")
# # class H(D,C,E):
# #     def g_details(self):
# #         print("H class")

# c1=C()
# c1.b_details()
# c1.a_details()
# c1.c_details()

# b1=B()
# b1.a_details()
# b1.b_details()

# d1=D()
# d1.b_details()
# d1.a_details()
# d1.d_details()

# e1=E()
# e1.b_details()
# e1.a_details()
# e1.e_details()

# f1=F()
# f1.a_details()
# f1.b_details()
# f1.f_details()
# f1.e_details()
# f1.c_details()


# class A:
#     def a_details(self):
#         print("Class A")
# class B(A):
#     def b_details(self):
#         print("Class B")
# class C(A):
#     def c_details(self):
#         print("Class C")
# class D(B,C):
#     def d_details(self):
#         print("Class D")
# d=D()
# d.a_details()
# d.b_details()
# d.c_details()
# d.d_details()
