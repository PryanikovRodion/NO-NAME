

class Product:
    def __init__(self,name:str,price:float,count:int):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        elif not isinstance(price,(int,float)):
            raise TypeError("price should be type:int or float")
        elif not isinstance(count,int):
            raise TypeError("count should be type:int")
        elif price <= 0:
            raise ValueError("price should be bigest of zero")
        elif count < 0:
            raise ValueError("count should be bigest or equal of zero")
        self.__name = name
        self.__price = price
        self.__count = count
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        self.__name = name

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self,count):
        if not isinstance(count,int):
            raise TypeError("count should be type:int")
        elif count < 0:
            raise ValueError("count should be bigest or equal of zero")

        self.__count = count

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        if not isinstance(price,(int,float)):
            raise TypeError("price should be type:int or float")
        elif price <= 0:
            raise ValueError("price should be bigest of zero")
        self.__price = price


    def __hash__(self):
        return str(self).__hash__()
    
    def __repr__(self):
        return f"|{self.__name}|{self.__price}$|{self.__count}|"    

class Saler:
    names = {}
    def __init__(self,name,money,*products):
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
        self.__name = name
        self.__money = money
        self.__products = {product.name:product for product in products}
    
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
        for key in self.__products:
            self.__products[self.__products[key].name] = self.__products[key]
            del self.__products[key] 

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self,money):
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

    def __repr__(self):
        result = f"Saler: {self.__name}\nProducts:\n"
        for product in self.__products:
            result = result + str(self.__products[product]) + "\n"
        return result
    
    def __hash__(self):
        return str(self).__hash__()

class Buyer:
    def __init__(self,name,adress,money=0.0):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        elif not isinstance(adress,str):
            raise TypeError("adress should be type:str")
        elif not isinstance(money,(int,float)):
            raise TypeError("money should be type:int or float")
        self.__name = name
        self.__adress = adress
        self.__money = money  
    
    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money   
    
    @money.setter
    def money(self,money):
        if not isinstance(money,(int,float)):
            raise TypeError("money should be type:float")
        elif money < 0:
            raise ValueError("money should be bigest of zero")
        self.__money = money
    
    @property
    def adress(self):
        return self.__adress
    
    def __repr__(self):
        return f"Buyer:{self.__name}\nMoneys:{self.__money}$\nAdress:{self.__adress} \n"
    
    def __hash__(self):
        return str(self).__hash__()   
        
class Order:
    number = 0
    def __init__(self,saler,product,product_count,buyer):
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
    
    def __hash__(self):
        return str(self).__hash__()

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
    
    def transaction(self,saler,product,buyer,count_product):
        if saler not in self.__salers:
            raise ValueError("saler should be in salers")
        elif product not in self.salers[saler].products:
            raise ValueError("product should be in saler products")
        elif buyer not in self.buyers:
            raise ValueError("buyer should be in buyers")
        elif not isinstance(count_product,int):
            raise TypeError("count should be type:int")
        elif self.salers[saler].products[product].count < count_product:
            raise ValueError("count of product in saler should be bigest or equal of input count of product")
        elif self.buyers[buyer].money < count_product*self.salers[saler].products[product].price:
            raise ValueError("money of buyer should many or equal of price_product*count_product")
        
        SALER = self.salers[saler]
        BUYER = self.buyers[buyer]
        PRODUCT = SALER.products[product]
        COUNT = count_product
        PRICE = PRODUCT.price*COUNT
        
        SALER.money += PRICE 
        BUYER.money -= PRICE
        PRODUCT.count -= COUNT

        self.__orders.append(Order(SALER,PRODUCT,COUNT,BUYER))

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
    
    return "change buyer complete"

def main():
    

    saler1 = Saler("sal1",10,Product("c++",200,10),Product("comp",1800,10))
    saler2 = Saler("sal2",0,Product("comp",1100,20),Product("cpp",160,100))
    buyer1 = Buyer("buy1","Пушкина21Б",1000)
    buyer2 = Buyer("buy2","Шевченко30",3000)
    buyer3 = Buyer("buy3","Картафана40",100)
    MAGAZIN = Magazin("Rozetka",[buyer1,buyer2,buyer3],[saler1,saler2])
    
    
    print("exit - завершает работу, выводя список заказов")
    print("salers - выводит список продавцов")
    print("search salers - выводит список продавцов продающих нужный вам товар")
    print("buy product - совершает покупку")
    print("buyers - выводит список покупателей")
    print("orders - выводит список заказов")
    print("change buyer - изменяет характеристики покупателей")
    #print("change saler")
    #print("add buyer - добавляет покупателя")
    #print("add saler - добавляет продавца")

    
    while True:
        comand = input("> ")
        if comand == "salers":
            print("_ "*60)
            for saler in MAGAZIN.salers:
                print(MAGAZIN.salers[saler])
            print("_ "*60)
        elif comand == "buyers":
            print("_ "*60)
            for buyer in MAGAZIN.buyers:
                print(MAGAZIN.buyers[buyer])
            print("_ "*60)

        elif comand == "search salers":
            product_name = input("product> ")
            print("_ "*60)
            for saler in MAGAZIN.search_salers(product_name):
                print(saler)
            print("_ "*60)

        elif comand == "buy product":
            print("_ "*60)
            try:
                product = input("product> ")
                saler = input("saler name> ")
                buyer = input("buyer name> ")
                count_product = int(input("count of product> "))
                MAGAZIN.transaction(saler,product,buyer,count_product)
            except Exception as error:
                print(f"ERROR:{error}\nTry again please\n")
            else:
                print("transaction complete")
            print("_ "*60)
            
        elif comand == "change buyer":
            print("_ "*60)
            try:
                print(change_buyers(MAGAZIN))
            except Exception as error:
                print(f"ERROR:{error}\nTry again please\n")
            print("_ "*60)
            
        elif comand == "orders":
            print("_ "*60)
            for order in MAGAZIN.orders:
                print(order)
            print("_ "*60)

        elif comand == "exit":
            print("_ "*60)
            for order in MAGAZIN.orders:
                print(order)

            print("_ "*60)
            break

        else: continue
   

if __name__ == "__main__":
    main()
    
    