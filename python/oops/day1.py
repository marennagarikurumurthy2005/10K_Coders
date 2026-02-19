class bike:
    color="red"
    type="with gears"
    price=120000
    name="Splender"
    def bike_behav(self):
        print(self.price)
        print(self.name)
ob1=bike()
ob1.bike_behav()
bike_color=ob1.color
print(bike_color)

class laptop:
    color="silver"
    size="14x16"
    ram="16GB"
    cpu="12C8T"
    def behav1(self):
        print(self.color)
        print(self.cpu)
    def behav2(self):
        print(self.ram)
        print(self.size)
obj2=laptop()
obj2.behav1()
obj2.behav2()
print(obj2.color)
print(obj2.cpu)

#  same for mobile , car

class  employee:
    name="KARTHIK"
    id="0236548"
    salary=75000
    shift="morning"
    joined="01-01-2023"
    
    def behav1(self):
        print(self.name)
    
    def behav2(self):
        print(self.name," is a senior developer")
obj3=employee()
obj3.behav1()
obj3.behav2()
print(obj3.salary)

