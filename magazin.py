from saler import Saler
from buyer import Buyer
from product import Product
from order import Order
import threading

class Magazin:
    instance = None

    def __del__(self):
        type(self).instance = None

    def __init__(self,name:str,buyers:list[Buyer],salers:list[Saler]):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        elif not isinstance(salers,list):
            raise TypeError("salers should be type:list")
        elif not isinstance(buyers,list):
            raise TypeError("buyers should be type:list")
        elif any(not isinstance(obj,Buyer)for obj in buyers):
            raise TypeError("All objects in buyers should be type:Buyer")
        elif any(not isinstance(obj,Saler)for obj in salers):
            raise TypeError("All objects in salers should be type:Saler")
        self.__name = name
        self.__buyers = {buyer.name:buyer for buyer in buyers}
        self.__salers = {saler.name:saler for saler in salers}
        self.__orders = []
        self.lock = threading.Lock()
    
    def __new__(cls,*args,**kwargs):
        if Magazin.instance is None:
            Magazin.instance = super().__new__(cls)
        return Magazin.instance
    
    def search_salers(self,name):
        
        for saler in self.__salers:
            if name in self.__salers[saler].products:
                yield self.__salers[saler]
        
    
    @property
    def salers(self):
        return self.__salers

    @property
    def buyers(self):
        return self.__buyers
    
    @property
    def orders(self):
        return self.__orders
    
    def transaction(self,saler_name,product_name,buyer_name,count_product):
        with self.lock:
            if saler_name not in self.__salers:
                raise ValueError("saler should be in salers")
            elif product_name not in self.salers[saler_name].products:
                raise ValueError("product should be in saler products")
            elif buyer_name not in self.buyers:
                raise ValueError("buyer should be in buyers")
            elif not isinstance(count_product,int):
                raise TypeError("count should be type:int")
            elif self.salers[saler_name].products[product_name].count < count_product:
                raise ValueError("count of product in saler should be bigest or equal of input count of product")
            elif self.buyers[buyer_name].money < count_product*self.salers[saler_name].products[product_name].price:
                raise ValueError("money of buyer should many or equal of price_product*count_product")
            
            
            saler = self.salers[saler_name]
            buyer = self.buyers[buyer_name]
            product = saler.products[product_name]
            price = product.price*count_product
                
            saler.money += price 
            buyer.money -= price
            product.count -= count_product

            self.__orders.append(Order(saler,product,count_product,buyer))

    def __repr__(self):
        return f"{self.__name}/{self.__buyers}/{self.__salers}"  
    

def change_buyers(magazin):
    buyer_name = input("name of buyer> ")
    if buyer_name in magazin.buyers:
        print("what you want to change in buyer?")
        print("name, money, adress")
        atribute = input("> ")
    else:
        return f"magazin not have a buyer with name {buyer_name}"
    if atribute == "name":
        new_name = input("new name> ")
        magazin.buyers[buyer_name].name = new_name
        magazin.buyers[new_name] = magazin.buyers[buyer_name]
        del magazin.buyers[buyer_name]
    elif atribute == "money":
        money = int(input("money> "))
        magazin.buyers[buyer_name].money += money
    elif atribute == "adress":
        adress = input("adress> ")
        magazin.buyers[buyer_name].adress = adress
    
    return "change buyer complete"