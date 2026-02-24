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
        
        
        
        

    


        
        



