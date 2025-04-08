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
    
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("name should be type:str")
        self.__name = name

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
    
    @adress.setter
    def adress(self,adress):
        if not isinstance(adress,str):
            raise TypeError("adress should be type:str")
        self.__adress = adress

    def __repr__(self):
        return f"Buyer:{self.__name}\nMoneys:{self.__money}$\nAdress:{self.__adress} \n"
    
    def __hash__(self):
        return str(self).__hash__()