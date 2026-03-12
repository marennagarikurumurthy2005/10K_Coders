from abc import abstractmethod,ABC

class shop(ABC):
    @abstractmethod
    def addtocart(self):
        pass
    @abstractmethod
    def cartsum(self):
        pass
class flip:
    def __init__(self,product_id,name,price,q):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.q=q
class flipcost(shop):
    cart_items=[]
    def addtocart(self,items):
        self.cart_items.append(items)
        print("Item added to cart")
    def cartsum(self):
        total_price=0
        for p in self.cart_items:
            total_price+=p.price*p.q
        print(total_price)

f1=flip(1,"mobile",20000,2)
f2=flip(2,"laptop",20000,1)
fs=flipcost()
fs.addtocart(f1)
fs.addtocart(f2)
fs.cartsum()         
        