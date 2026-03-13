from abc import abstractmethod,ABC

# class shop(ABC):
#     @abstractmethod
#     def addtocart(self):
#         pass
#     @abstractmethod
#     def cartsum(self):
#         pass
# class flip:
#     def __init__(self,product_id,name,price,q):
#         self.product_id=product_id
#         self.name=name
#         self.price=price
#         self.q=q
# class flipcost(shop):
#     cart_items=[]
#     def addtocart(self,items):
#         self.cart_items.append(items)
#         print("Item added to cart")
#     def cartsum(self):
#         total_price=0
#         for p in self.cart_items:
#             total_price+=p.price*p.q
#         print(total_price)

# f1=flip(1,"mobile",20000,2)
# f2=flip(2,"laptop",20000,1)
# fs=flipcost()
# fs.addtocart(f1)
# fs.addtocart(f2)
# fs.cartsum()   



class bank(ABC):
    @abstractmethod
    def add_cus(self):
        pass
    def update_details(self):
        pass
    def credit(self):
        pass
    def debit(self):
        pass
    def avail_bal(self):
        pass
class customer:
    def __init__(self,id,name,amount,main_pin):
        self.id=id
        self.name=name
        self.amount=amount
        self.main_pin=main_pin
class cust_set(bank):
    cust_details=[]
    
        
        