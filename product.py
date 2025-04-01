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
            raise ValueError("count should be bigest of zero")
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