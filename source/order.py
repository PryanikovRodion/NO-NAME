from source.saler import Saler
from source.buyer import Buyer
from source.product import Product

class Order:
    number = 0
    def __init__(self,saler:Saler,product:Product,product_count:int,buyer:Buyer):
        if not isinstance(saler,Saler):
            raise TypeError("saler should be type:Saler")
        elif not isinstance(product,Product):
            raise TypeError("product should be type:Product")
        elif not isinstance(product_count,int):
            raise TypeError("product_count should be type:int")
        elif not isinstance(buyer,Buyer):
            raise TypeError("buyer should be type:Buyer")
        self.__number = Order.number
        Order.number += 1
        self.__saler = saler
        self.__buyer = buyer
        self.__product = product
        self.__product_count = product_count
    
    def __repr__(self):
        result = f"Order:{self.__number}\n"
        result += f"Product name:{self.__product.name}\n"
        result += f"Count of Product:{self.__product_count}\n"
        result += f"Saler:{self.__saler.name}\n"
        result += f"Buyer:{self.__buyer.name}\n"
        result += f"Buyer adress:{self.__buyer.adress}\n"
        return result
    
    @property
    def saler(self):
        return self.__saler
    
    @property
    def buyer(self):
        return self.__buyer
    
    def __hash__(self):
        return str(self).__hash__()