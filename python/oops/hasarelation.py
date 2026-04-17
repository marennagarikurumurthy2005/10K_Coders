# class animal:
#     def __init__(self,sound,type):
#         self.sound=sound
#         self.type=type
    
#     def beh(self):
#         print(self.sound)
#         print(self.type)
# class dog:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def behv(self):
#         animal("bow","pet").beh()
#         print(self.name)
#         print(self.color)
# d=dog("lyca","WHite")
# d.behv()


# class cat:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def behav(self):
#         animal("meow","pet").beh()
#         print(self.name,self.color)

# c=cat("lucifer","black")
# c.behav()
        




class cse:
    def __init__(self,strength,block):
        self.strength=strength
        self.block=block
    def cse_details(self):
        print("CSE DETAILS")
        print(self.strength)
        print(self.block)


class mech:
    def __init__(self,strength,block):
        self.strength=strength
        self.block=block
    def mech_details(self):
        print("MECH DETAILS")
        print(self.strength)
        print(self.block)

class ece:
    def __init__(self,strength,block):
        self.strength=strength
        self.block=block
    def ece_details(self):
        print("ECE DETAILS")
        print(self.strength)
        print(self.block)
        

class college:
    def __init__(self,cse_obj,mech_obj,ece_obj):
        self.cse_obj=cse_obj
        self.mech_obj=mech_obj
        self.ece_obj=ece_obj
    def college_details(self):
        print("MRITS")
        self.cse_obj.cse_details()
        self.mech_obj.mech_details()
        self.ece_obj.ece_details()


c1=cse(120,1)
m1=mech(120,2)
e1=ece(10,3)
d1=college(c1,m1,e1)
d1.college_details()
        
        


class window_8:
    def __init__(self,release_date,update_size):
        self.release_date=release_date
        self.update_size=update_size

    def window_8_details(self):
        print(self.release_date)
        print(self.update_size) 

class window_10:
    def __init__(self,release_date,update_size):
        self.release_date=release_date
        self.update_size=update_size

    def window_10_details(self):
        print(self.release_date)
        print(self.update_size) 

class window_11:
    def __init__(self,release_date,update_size):
        self.release_date=release_date
        self.update_size=update_size

    def window_11_details(self):
        print(self.release_date)
        print(self.update_size) 

class microsoft:
    def __init__(self,win_8,win_10,win_11):
        self.win_8=win_8
        self.win_10=win_10
        self.win_11=win_11

    def microsoft_window_versions(self):
        self.win_8.window_8_details()
        self.win_10.window_10_details()
        self.win_11.window_11_details()

w8=window_8("26 October 2012","3.5 gb")

w10=window_10("29 July 2015","4 gb")

w11=window_11("5 October 2021","6 gb")

m1=microsoft(w8,w10,w11)

m1.microsoft_window_versions()
    
class redmi:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price

    def redmi_details(self):
        print(self.pname)
        print(self.price)

class samsung:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price

    def samsung_details(self):
        print(self.pname)
        print(self.price)

class rog:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price

    def rog_details(self):
        print(self.pname)
        print(self.price)

class phones:
    def __init__(self,redmi,samsung,rog):
        self.redmi=redmi
        self.samsung=samsung
        self.rog=rog

    def phone_details(self):
        self.redmi.redmi_details()
        self.samsung.samsung_details()
        self.rog.rog_details()

p1=redmi("redmi note 10s",1500)   
p2=samsung("s25 ultra",150000)
p3=rog("rog 7",70000)     
        
m1=phones(p1,p2,p3)

m1.phone_details()



class student1:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def student1_details(self):
        print("Student1 Details")
        print(self.name)
        print(self.number)
class student2:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def student2_details(self):
        print("Student2 Details")
        print(self.name)
        print(self.number)
class institute:
    def __init__(self,student1_obj,student2_obj):
        self.student1_obj=student1_obj
        self.student2_obj=student2_obj
    def inst_details(self):
        print("MRITS CSE-DS")
        self.student1_obj.student1_details()
        self.student2_obj.student2_details()
        

s1=student1("MK",9705558556)
s2=student2("RK",7989020757)
i=institute(s1,s2)
i.inst_details()

        
    
        
        
        

    


        
        



