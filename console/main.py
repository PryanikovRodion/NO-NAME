import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from source.saler import Saler
from source.buyer import Buyer
from source.product import Product
from source.magazin import Magazin
import threading

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

def main():
    saler1 = Saler("sal1",10,Product("c++",200,1000),Product("comp",1800,1000))
    saler2 = Saler("sal2",0,Product("comp",1100,2000),Product("cpp",160,1000))
    buyer1 = Buyer("buy1","Пушкина21Б",10000)
    buyer2 = Buyer("buy2","Шевченко30",10000)
    buyer3 = Buyer("buy3","Картафана40",10000)
    magaz = Magazin("Rozetka",[buyer1,buyer2,buyer3],[saler1,saler2])
    
    
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

    threads = []
    while True:
        comand = input("> ")
        if comand == "salers":
            print("_ "*60)
            for saler in magaz.salers:
                print(magaz.salers[saler])
            print("_ "*60)
        elif comand == "buyers":
            print("_ "*60)
            for buyer in magaz.buyers:
                print(magaz.buyers[buyer])
            print("_ "*60)

        elif comand == "search salers":
            product_name = input("product> ")
            print("_ "*60)
            for saler in magaz.search_salers(product_name):
                print(saler)
            print("_ "*60)

        elif comand == "buy product":
            print("_ "*60)
            try:
                product_name = input("product> ")
                saler_name = input("saler name> ")
                buyer_name = input("buyer name> ")
                count_product = int(input("count of product> "))
                #MAGAZIN.transaction(saler,product,buyer,count_product)
                thread = threading.Thread(target=magaz.transaction,args=(saler_name,product_name,buyer_name,count_product))
                threads.append(thread)
                thread.start()

            except Exception as error:
                print(f"ERROR:{error}\nTry again please\n")
            else:
                print("transaction complete")
            print("_ "*60)
            
        elif comand == "change buyer":
            print("_ "*60)
            try:
                print(change_buyers(magaz))
            except Exception as error:
                print(f"ERROR:{error}\nTry again please\n")
            print("_ "*60)
            
        elif comand == "orders":
            print("_ "*60)
            for order in magaz.orders:
                print(order)
            print("_ "*60)

        elif comand == "exit":
            print("_ "*60)
            for order in magaz.orders:
                print(order)
            print("salers balances:")
            for saler in magaz.salers:
                print(magaz.salers[saler].name,"-",magaz.salers[saler].money)

            print("_ "*60)
            break

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()