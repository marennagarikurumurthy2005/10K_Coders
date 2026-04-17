from abc import ABC,abstractmethod
class person(ABC):
    @abstractmethod
    def add_details(self):
        pass
    @abstractmethod
    def update_details(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    def view(self):
        pass

# class employee:
#     def __init__(self,id,name,sal):
#         self.id=id
#         self.name=name
#         self.sal=sal
# class employee_management(person):
#     details=[]
   
#     def add_details(self,items):
        
#         self.details.append(items)
#         print("added")
#     def update_details(self,id,**kwargs):
        
#         for s in self.details:
#             if id==s.id:
#                 if "name" in kwargs:
#                     s.name=kwargs["name"]
#                 if "new_id" in kwargs:
#                     s.id=kwargs["new_id"]
#                 if "sal" in kwargs:
#                     s.sal=kwargs["sal"]
#                 print("Details updated")
#                 return
#         else:
#             print("ID not found")
#     def delete(self,id):
#         for s in self.details:
#             if s.id==id:
#                 self.details.remove(s)
#                 print("Deleted")
#                 return
#     def view(self):
#         for s in self.details:
#             print(s.id,end=", ")
#             print(s.name,end=", ")
#             print(s.sal)

# e1=employee(1,"MK",26000)
# e3=employee(2,"GK",50000)
# e2=employee_management()
# e2.add_details(e1)
# e2.add_details(e3)
# e2.view()
# e2.update_details(2,new_id=40,name="TK",sal=260000)
# e2.view()

class student:
    def __init__(self,id,name,branch,fee_paid):
        self.id=id
        self.name=name
        self.branch=branch
        self.fee_paid=fee_paid
class student_manage(person):
    details=[]
    def add_details(self,items):
        self.details.append(items)
        print("Details added")
    def update_details(self,id,**kwargs):
        for s in self.details:
            if s.id==id:
                if "new_id" in kwargs:
                    s.id=kwargs["new_id"]
                if "name" in kwargs:
                    s.name=kwargs["name"]
                if "branch" in kwargs:
                    s.branch=kwargs["branch"]
                if "fee_paid" in kwargs:
                    s.fee_paid=kwargs["fee_paid"]
                print("Update")
                return
        else:
            print("Invalid ID")
    def delete(self,id):
        for s in self.details:
            if s.id==id:
                self.details.remove(s)
                print("delete success")
                return
    def view(self):
        for s in self.details:
            print(s.id,end=", ")
            print(s.name,end=", ")
            print(s.branch,end=", ")
            print(s.fee_paid)

s1=student(24,"Murthy","DS",0)
sm1=student_manage()
sm1.add_details(s1)
sm1.view()
        
    


        
















        

            

        
    
        
        
        
    




# class emp_det(employee):
#     details=[]
#     def __init__(self,id,name,sal):
#         self.id=id
#         self.name=name
#         self.sal=sal

#     def add_details(self):
#         if self.id not in self.details:
#             self.details.append(self.id)
#             print("DEtails added")
#         else:
#             print("Id exist")

#     def update_details(self,id,new_id,**kwargs):
#         if self.id==id:
#             for s in kwargs:
#                 self.id=new_id
                
#     def delete(self,id):
#         for i in self.details:
#             if self.id==id:
#                 self.details.remove(i)
#                 print("delete successfully")

#     def view(self):
#         print(self.details)

# s1=emp_det(1,"MK",25000)
# s1.add_details()
# s1.view()


        

        
        
        