from source.product import Product
import threading

class Saler:
    names = set()
    def __init__(self,name:str,money:(int|float)=0,*products):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        elif not all(isinstance(obj,Product) for obj in products):
            raise TypeError("All objects in products should be type:Product")
        elif not isinstance(money,(int,float)):
            raise TypeError("money should be type:int or float")
        elif name in Saler.names:
            raise ValueError("name should be unique")
        elif money < 0:
            raise ValueError("money should be bigest or equal of zero")
        if not all(isinstance(obj,Product) for obj in products):
            raise TypeError("All objects in products should be type:Product")
        
        product_names = set()
        for product in products:
            if product.name in product_names:
                raise Warning("name of product in one saler should unique")
            product_names.add(product.name)
        
        Saler.names.add(name)
        self.__name = name
        self.__money = money
        self.__products = {product.name:product for product in products}
        self.lock = threading.Lock()
    
    @property
    def products(self):
        return self.__products
    
    @products.setter
    def products(self,*products):
        if not all(isinstance(obj,Product) for obj in products):
            raise TypeError("All objects in products should be type:Product")
        product_names = set()
        for product in products:
            if product.name in product_names:
                raise Warning("name of product in one saler should unique")
            product_names.add(product.name)
        self.__products = {product.name:product for product in products}
    
    def update_products(self):
        oldkeylist = []
        for key in self.__products.keys():
            new_key =self.__products[key].name
            self.__products[new_key] = self.__products[key]
            if new_key != key:
                oldkeylist.append(key)
        for key in oldkeylist:
            del self.__products[key]

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self,money):
        with self.lock:
            if not isinstance(money,(int,float)):
                raise TypeError("money should be type:int or float")
            elif money < 0:
                raise ValueError("money should be bigest or equal of zero")
            self.__money = money
    
    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        elif name in Saler.names:
            raise ValueError("name should be unique")
        del Saler.names[self.__name]
        self.__name = name
        Saler.names[self.__name]

    def __repr__(self):
        result = f"Saler: {self.__name}\nProducts:\n"
        for product in self.__products:
            result = result + str(self.__products[product]) + "\n"
        return result
    
    def __hash__(self):
        return str(self).__hash__()