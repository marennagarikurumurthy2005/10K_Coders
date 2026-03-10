from abc import ABC,abstractmethod
class person:
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

class employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
class employee_management(person):
    details=[]
    def add_details(self,items):
        self.details.append(items)
        print("added")
    def update_details(self,id,**kwargs):
        for s in self.details:
            if s.id==id:
                if "name" in kwargs:
                    s.name=kwargs["Name"]
                if "new_id" in kwargs:
                    s.id=kwargs["new_id"]
                if "sal" in kwargs:
                    s.sal=kwargs["sal"]
                print("Details updated")
            return
        else:
            print("ID not found")
    def delete(self,id):
        for s in self.details:
            if s.id==id:
                self.details.remove(s)
                print("Deleted")
                return
    def view(self):
        for s in self.details:
            print(s.id)
            print(s.name)
            print(s.sal)

e1=employee(1,"MK",26000)
e3=employee(2,"GK",50000)
e2=employee_management()
e2.add_details(e1)
e2.add_details(e3)
e2.view()
e2.update_details(2,new_id=40,Name="TK",sal=260000)
e2.view()


        

            

        
    
        
        
        
    




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


        

        
        
        