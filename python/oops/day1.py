# class bike:
#     color="red"
#     type="with gears"
#     price=120000
#     name="Splender"
#     def bike_behav(self):
#         print(self.price)
#         print(self.name)
# ob1=bike()
# ob1.bike_behav()
# bike_color=ob1.color
# print(bike_color)

# class laptop:
#     color="silver"
#     size="14x16"
#     ram="16GB"
#     cpu="12C8T"
#     def behav1(self):
#         print(self.color)
#         print(self.cpu)
#     def behav2(self):
#         print(self.ram)
#         print(self.size)
# obj2=laptop()
# obj2.behav1()
# obj2.behav2()
# print(obj2.color)
# print(obj2.cpu)

# #  same for mobile , car

# class  employee:
#     name="KARTHIK"
#     id="0236548"
#     salary=75000
#     shift="morning"
#     joined="01-01-2023"
    
#     def behav1(self):
#         print(self.name)
    
#     def behav2(self):
#         print(self.name," is a senior developer")
# obj3=employee()
# obj3.behav1()
# obj3.behav2()
# print(obj3.salary)


class student:
    institute="10K Coders"
    def __init__(self,name,course,session,pm):
        self.name=name
        self.course=course
        self.session=session
        self.pm=pm
    def details(self):
        print(self.institute,end=" ")
        print(self.name,end=" ")
        print(self.course, end=" ")
        print(self.session,end=" ")
        print(self.pm,end=" ")
        print()
        print()
s1=student("kurumurthy","PFS","AM","Abdul")
s2=student("Vignesh","JFS","PM","sanny")
s3=student("Vamc","CS","PM","jansi")
s4=student("Yaseen","PFS","PM","suchi")
s5=student("anil","MERN","AM","Balu")
s1.details()
s2.details()
s3.details()
s4.details()
s5.details()




class employee:
    institute="10K Coders"
    def __init__(self,name,course,session,sal):
        self.name=name
        self.course=course
        self.session=session
        self.sal=sal
    def details(self):
        print(self.institute,end=" ")
        print(self.name,end=" ")
        print(self.course, end=" ")
        print(self.session,end=" ")
        print(self.sal,end=" ")
        print()
        print()
e1=employee("kurumurthy","PFS","AM",10000)
e2=employee("Vignesh","JFS","PM",50000)
e3=employee("Vamc","CS","PM",20000)
e4=employee("Yaseen","PFS","PM",60000)
e5=employee("anil","MERN","AM",55555)
e1.details()
e2.details()
e3.details()
e4.details()
e5.details()



class bank:
    b_name="SBI"
    def __init__(self,branch_name,location,session,manager):
        self.branch_name=branch_name
        self.location=location
        self.session=session
        self.manager=manager
    def details(self):
        print(self.b_name,end=" ")
        print(self.branch_name,end=" ")
        print(self.location, end=" ")
        print(self.session,end=" ")
        print(self.manager,end=" ")
        print()
        print()
b1=bank("SBI-KKT","Kothakota","10-5","Abdul")
b2=bank("SBI-WNP","wanparthy","10-5","sanny")
b3=bank("SBI-NIR","nirven","10-5","jansi")
b4=bank("SBI-AMT","atmakur","10-5","suchi")
b5=bank("SBI-VNR","konnur","10-5","Balu")
b1.details()
b2.details()
b3.details()
b4.details()
b5.details()