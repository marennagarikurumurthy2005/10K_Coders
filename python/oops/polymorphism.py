# method and constructor over-riding

# class vehicle:
#     def __init__(self,engine):
#         self.engine=engine
#     def details(self):
#         print(self.engine)
# class car(vehicle):
#     def __init__(self,engine):
#         self.engine=engine

#     def details(self):
#         print(self.engine)
# class bike(vehicle):
#     def __init__(self,engine):
#         self.engine=engine
#     def details(self):
#         print(self.engine)
# class truck(vehicle):
#     def __init__(self,engine):
#         self.engine=engine
#     def details(self):
#         print(self.engine)

# obj=truck("800cc")
# obj.details()



# Question 2

# class rbi:
#     def __init__(self,roi,amount):
#         self.roi=roi
#         self.amount=amount
#     def ROI(self):
#         print(self.roi)
#     def AMT(self):
#         print(self.amount)
# class sbi(rbi):
#     def __init__(self,r,a):
#         self.r=r
#         self.a=a
#     def ROI(self):
#         print(self.r)
#     def AMT(self):
#         print(self.a)
# class union(rbi):
#     def __init__(self,r,a):
#         self.r=r
#         self.a=a
#     def ROI(self):
#         print(self.r)
#     def AMT(self):
#         print(self.a)
# class hdfc(rbi):
#     def __init__(self,r,a):
#         self.r=r
#         self.a=a
#     def ROI(self):
#         print(self.r)
#     def AMT(self):
#         print(self.a)
# class canara(rbi):
#     def __init__(self,r,a):
#         self.r=r
#         self.a=a
#     def ROI(self):
#         print(self.r)
#     def AMT(self):
#         print(self.a)

# obj=canara("24%",40000)
# obj.ROI()
# obj.AMT()

# obj=rbi("24%",4000000)
# obj.ROI()
# obj.AMT()


# # constructor overriding

# class India:
#     def __init__(self):
#         print("India has 24 states")
#     def __init__(self):
#         print("India has 29 states")
# obj=India()
        

class student:
    def __init__(self,name,rnum,pnum,clg):
        self.name=name,
        self.rnum=rnum,
        self.pnum=pnum,
        self.clg=clg,
        dici={
            "name":self.name,
            "rnum":self.rnum,
            "pnum":self.pnum,
            "clg":self.clg
        }
    def create(self,**kwargs):

        

        for i,j in kwargs.item():
            i

    def view(self):
        print(self.name)
        print(self.clg)
        print(self.rnum)
        print(self.pnum)

    def update(self,**kwargs):
        pass
    

        

        