import tkinter as tk
from saler import Saler
from buyer import Buyer
from product import Product
from magazin import Magazin
from tkinter import messagebox as ms


WIDTH = 800
HEIGHT = 600
PADX = 16
PADY = 12
FONT_1 = ("Bauhaus 93", 24)
FONT_2 = ("Times New Roman", 24)
FONT_3 = ("Courier New", 24)
FONT_4 = ("Goudy Old Style", 18)
ICON_1 = "icon_1.png"
ICON_2 = "icon_2.png"
ICON_3 = "icon_3.png"
ICON_4 = "icon_4.png"
ICON_5 = "icon_5.png"

def clearWindow(i:int = 0):
    for widget in root.winfo_children()[i:]:
        widget.destroy()

def addMoneyBuyer(entMoney):
    try:
        sum = float(entMoney.get())
    except ValueError:
        ms.showerror("Error","Enter the number!")
    else:
        magaz.buyers[userName].money += sum
    finally:
        createAddMoneyBuyer()

def addProductSaler(entName,entPrice,entCount):
    name = entName.get()
    price = entPrice.get()
    count = entCount.get()
    if not name or not price or not count:
        ms.showerror("Error","Enter name of product, price of product and count of product")
        createAddProductSaler()
        return None
    try:
        magaz.salers[userName].products[name] = Product(name,float(price),int(count))
        magaz.salers[userName].update_products()
        createAddProductSaler()
    except TypeError as error:
        ms.showerror("Error",error)
    except ValueError as error:
        ms.showerror("Error",error)
    finally:
        createAddProductSaler()
        

def BuyProductBuyer(entSalerName,entProductName,entCountProduct):
    saler_name = entSalerName.get()
    product_name = entProductName.get()
    count_product = entCountProduct.get()
    if not saler_name or not product_name or not count_product:
        ms.showerror("Error","Enter saler name, product name and count of product.") 
        createBuyProductBuyer()
        return None
    try:
        count_product = int(count_product)
        magaz.transaction(saler_name,product_name,userName,count_product)
        createBuyProductBuyer()
    except TypeError:
        ms.showerror("Error","Count of product should be integer number!")
    except ValueError as error:
        ms.showerror("Error",error)
    finally:
        createBuyProductBuyer()
        return None
    
def createAddMoneyBuyer():
    clearWindow(1)
    lblMoney = tk.Label(root,text="Sum of money:",font=FONT_3)
    entMoney = tk.Entry(root,font=FONT_2)
    btnAdd = tk.Button(root,text="ADD",font=FONT_3,command=lambda:addMoneyBuyer(entMoney))
    lblMoney.pack(pady=PADY)
    entMoney.pack(pady=PADY)
    btnAdd.pack(padx=PADX,pady=PADY)

def createAddProductSaler():
    clearWindow(1)
    entName = tk.Entry(root,font=FONT_2)
    entPrice = tk.Entry(root,font=FONT_2)
    entCount = tk.Entry(root,font=FONT_2)
    lblName = tk.Label(root,text="Name product:",font=FONT_2)
    lblPrice = tk.Label(root,text="Price product:",font=FONT_2)
    lblCount = tk.Label(root,text="Count product:",font=FONT_2)
    btnAdd = tk.Button(root,text="ADD",font=FONT_2,command=lambda:addProductSaler(entName,entPrice,entCount))
    lblName.pack()
    entName.pack()
    lblPrice.pack()
    entPrice.pack()
    lblCount.pack()
    entCount.pack()
    btnAdd.pack()

def createBuyProductBuyer(product_name:str="",saler_name:str=""):
    clearWindow(1)
    entProductName = tk.Entry(root,font=FONT_4)
    entSalerName = tk.Entry(root,font=FONT_4)
    entCountProduct = tk.Entry(root,font=FONT_4)
    btnBuy = tk.Button(root,text="BUY",font=FONT_2,command=lambda:BuyProductBuyer(entSalerName,entProductName,entCountProduct))
    tk.Label(root,text=f"Your balance: {magaz.buyers[userName].money}",font=FONT_2).pack()
    tk.Label(root,text="Product:",font=FONT_2).pack(fill="x",padx=PADX,pady=PADY)
    entProductName.pack()
    tk.Label(root,text="Saler:",font=FONT_2).pack(fill="x",padx=PADX,pady=PADY)
    entSalerName.pack()
    tk.Label(root,text="Count:",font=FONT_2).pack(fill="x",padx=PADX,pady=PADY)
    entCountProduct.pack()
    btnBuy.pack(padx=PADX,pady=PADY)
    if product_name:entProductName.insert(0,product_name)
    if entSalerName:entSalerName.insert(0,saler_name)

def createClientBuyer(buyer_name=None):
    clearWindow()
    if buyer_name:
        global userName
        userName = buyer_name
    root.title(f"Client of {userName}")
    menu = tk.Menu(root,title="menu")
    menu.add_command(label="INFO",command = lambda:createClientBuyer())
    menu.add_command(label="ADD MONEY",command = lambda:createAddMoneyBuyer())
    menu.add_command(label="SALERS",command = lambda:createSalersListBuyer())
    menu.add_command(label="BUY PRODUCT",command= lambda:createBuyProductBuyer())
    menu.add_command(label="ORDERS",command= lambda:createOrders("b"))
    menu.add_separator()
    menu.add_command(label="exit",command=lambda:createLoginLogout())
    root.config(menu=menu)
    createInfoBuyer()
    
def createClientSaler(saler_name=None):
    clearWindow()
    if saler_name:
        global userName
        userName = saler_name
    root.title(f"Client of {userName}")
    menu = tk.Menu(root)
    menu.add_command(label="INFO",command=lambda:createInfoSaler())
    menu.add_command(label="PRODUCTS",command=lambda:createProductsSaler())
    menu.add_command(label="ADD PRODUCT",command=lambda:createAddProductSaler())
    menu.add_command(label="exit",command=lambda:createLoginLogout())
    root.config(menu=menu)
    createInfoSaler()

def createInfoBuyer():
    clearWindow(1)
    tk.Label(root,text=f"Name: {magaz.buyers[userName].name}",font=FONT_2).pack(expand=True,fill="both",anchor="nw",padx=PADX,pady=PADY)
    tk.Label(root,text=f"Adress: {magaz.buyers[userName].adress}",font=FONT_2).pack(expand=True,fill="both",anchor="nw",padx=PADX,pady=PADY)
    tk.Label(root,text=f"Balance: {magaz.buyers[userName].money}",font=FONT_2).pack(expand=True,fill="both",anchor="nw",padx=PADX,pady=PADY)

def createInfoSaler():
    clearWindow(1)
    tk.Label(root,text=f"Name: {magaz.salers[userName].name}",font=FONT_2).pack(expand=True,fill="both",anchor="nw",padx=PADX,pady=PADY)
    tk.Label(root,text=f"Balance: {magaz.salers[userName].money}",font=FONT_2).pack(expand=True,fill="both",anchor="nw",padx=PADX,pady=PADY)

def createOrders(key: str):
    clearWindow(1)
    listUserOrders = magaz.user_orders(key, userName)
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=PADX, pady=PADY)
    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    scrollable_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    for order in listUserOrders:
        order_frame = tk.Frame(scrollable_frame, relief=tk.RIDGE, borderwidth=2)
        order_frame.pack(fill=tk.X, padx=PADX, pady=PADY)
        tk.Label(order_frame, text=str(order), font=FONT_2).pack(anchor="w", padx=PADX, pady=PADY)
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
def createLogoutSaler():
    clearWindow(3)
    root.title("Registraete Saler")
    lblName = tk.Label(root,text="name of saler:",font=FONT_3)
    entName = tk.Entry(root)
    btnReg = tk.Button(root,text="registrate",font=FONT_3,command=lambda:registrate(varUser,entName))
    btnBack = tk.Button(root,text="Go Back",font=FONT_3,command=lambda:createLoginLogout())
    lblName.pack(expand=True,fill="both")
    entName.pack(fill="x",padx=PADX)
    btnReg.pack(expand=True,fill="both",padx=PADX,pady=PADY)
    btnBack.pack(expand=True,fill="both",padx=PADX,pady=PADY)

def createLogoutBuyer():
    clearWindow(3)
    root.title("Registraete Buyer")
    lblName = tk.Label(root,text="name of buyer:",font=FONT_3)
    entName = tk.Entry(root)
    lblAdress = tk.Label(root,text="adress of buyer:",font=FONT_3)
    entAdress = tk.Entry(root)
    btnReg = tk.Button(root,text="registrate",font=FONT_3,command=lambda:registrate(varUser,entName,entAdress))
    btnBack = tk.Button(root,text="Go Back",font=FONT_3,command=lambda:createLoginLogout())
    lblName.pack(expand=True,fill="both")
    entName.pack(fill="x",padx=PADX)
    lblAdress.pack(expand=True,fill="both")
    entAdress.pack(fill="x",padx=PADX)
    btnReg.pack(expand=True,fill="both",padx=PADX,pady=PADY)
    btnBack.pack(expand=True,fill="both",padx=PADX,pady=PADY)

def createSalersListBuyer0():
    clearWindow(1)
    def selection(event):
        listbox = event.widget
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_text = listbox.get(selected_indices[0])
            createBuyProductBuyer(selected_text.split("|")[1],listbox.winfo_name())
    listboxes = []
    for saler in magaz.salers.values():
        tk.Label(root,text = saler.name,font=FONT_2).pack()
        listbox = tk.Listbox(root, height=len(saler.products),font=FONT_2,name=saler.name)
        listbox.pack(padx=PADX, pady=PADY, anchor="center")
        for product in saler.products.values():
            listbox.insert(tk.END,product)
        listbox.bind("<<ListboxSelect>>", selection)
        listboxes.append(listbox)

def createSalersListBuyer1():
    clearWindow(1)

    def selection(event):
        listbox = event.widget
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_text = listbox.get(selected_indices[0])
            createBuyProductBuyer(selected_text.split("|")[1], listbox.winfo_name())

    listboxes = []
    
    for saler in magaz.salers.values():
        tk.Label(root, text=saler.name, font=FONT_2).pack()

        # Фрейм для Listbox и Scrollbar
        frame = tk.Frame(root)
        frame.pack(padx=PADX, pady=PADY, anchor="center")

        # Listbox внутри Frame
        listbox = tk.Listbox(frame, height=10, font=FONT_2, name=saler.name)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar внутри Frame
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Связываем Listbox и Scrollbar
        listbox.config(yscrollcommand=scrollbar.set)

        # Заполняем Listbox товарами
        for product in saler.products.values():
            listbox.insert(tk.END, product)

        listbox.bind("<<ListboxSelect>>", selection)
        listboxes.append(listbox)   

def createSalersListBuyer():
    clearWindow(1)
    def selection(event):
        listbox = event.widget
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_text = listbox.get(selected_indices[0])
            createBuyProductBuyer(selected_text.split("|")[1], listbox.winfo_name())
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=PADX, pady=PADY)
    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    scrollable_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    listboxes = []
    for saler in magaz.salers.values():
        saler_frame = tk.Frame(scrollable_frame, relief=tk.RIDGE, borderwidth=2)
        saler_frame.pack(fill=tk.X, padx=PADX, pady=PADY)
        tk.Label(saler_frame, text=saler.name, font=FONT_2).pack(anchor="w", padx=PADX, pady=PADY)
        frame = tk.Frame(saler_frame)
        frame.pack(fill=tk.X, padx=PADX)
        listbox = tk.Listbox(frame, height=10, font=FONT_2, name=saler.name)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        list_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=list_scrollbar.set)
        for product in saler.products.values():
            listbox.insert(tk.END, product)
        listbox.bind("<<ListboxSelect>>", selection)
        listboxes.append(listbox)
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def createStore():
    saler1 = Saler("sal1",10,Product("c++",200,1000),Product("comp",1800,1000))
    saler2 = Saler("sal2",0,Product("comp",1100,2000),Product("cpp",160,1000))
    buyer1 = Buyer("buy1","Пушкина21Б",10000)
    buyer2 = Buyer("buy2","Шевченко30",10000)
    buyer3 = Buyer("buy3","Картафана40",10000)
    global magaz
    magaz = Magazin("Rozetka",[buyer1,buyer2,buyer3],[saler1,saler2])

def createProductsSaler():
    clearWindow(1)
    listbox = tk.Listbox(root, height=len(magaz.salers[userName].products),font=FONT_2)
    listbox.pack(padx=PADX, pady=PADY, fill="both",anchor="center")
    for product in magaz.salers[userName].products.values():
        listbox.insert(tk.END, str(product))

def createLogin():
    clearWindow()
    root.title("Login")
    lblDescription = tk.Label(root,text="You buyer or saler?",font=FONT_2)
    global varUser
    varUser = tk.StringVar(value="None") 
    radioBuyer = tk.Radiobutton(root, text="Buyer", variable=varUser, value="Buyer",font=FONT_3, command=lambda:createLoginBuyer())
    radioSaler = tk.Radiobutton(root, text="Saler", variable=varUser, value="Saler",font=FONT_3, command=lambda:createLoginSaler())
    btnBack = tk.Button(root,text="Go Back",font=FONT_3,command=lambda:createLoginLogout())
    lblDescription.pack(expand=True, fill="both", padx=PADX, pady=PADY)
    radioBuyer.pack(expand=True,fill="both",anchor="center", padx=PADX, pady=PADY)
    radioSaler.pack(expand=True,fill="both",anchor="center", padx=PADX, pady=PADY)
    btnBack.pack(expand=True, fill="both", padx=PADX, pady=PADY)

def createLogout():
    clearWindow()
    root.title("Logout")
    lblDescription = tk.Label(root,text="You buyer or saler?",font=FONT_2)
    global varUser
    varUser = tk.StringVar(value="None")  
    radioBuyer = tk.Radiobutton(root, text="Buyer", variable=varUser, value="Buyer",font=FONT_3, command=lambda:createLogoutBuyer())
    radioSaler = tk.Radiobutton(root, text="Saler", variable=varUser, value="Saler",font=FONT_3, command=lambda:createLogoutSaler())
    btnBack = tk.Button(root,text="Go Back",font=FONT_3,command=lambda:createLoginLogout())
    lblDescription.pack(expand=True, fill="both", padx=PADX, pady=PADY)
    radioBuyer.pack(expand=True,fill="both",anchor="center", padx=PADX, pady=PADY)
    radioSaler.pack(expand=True,fill="both",anchor="center", padx=PADX, pady=PADY)
    btnBack.pack(expand=True, fill="both", padx=PADX, pady=PADY)

def createLoginBuyer():
    clearWindow()
    def selection(event):
        selected_indices = listbox.curselection()  
        if selected_indices:
            selected_text = listbox.get(selected_indices[0])
            createClientBuyer(selected_text)
    listbox = tk.Listbox(root, height=len(magaz.buyers),font=FONT_2)
    listbox.pack(padx=PADX, pady=PADY, fill="both",anchor="center")
    for buyer in magaz.buyers:
        listbox.insert(tk.END, buyer)  
    label = tk.Label(root, text="Выберите элемент",font=FONT_2)
    label.pack(expand=True,pady=5)
    listbox.bind("<<ListboxSelect>>", selection)
    btnBack = tk.Button(root,text="Go Back",font=FONT_3,command=lambda:createLogin())
    btnBack.pack(expand=True, fill="both", padx=PADX, pady=PADY)

def createLoginSaler():
    clearWindow()
    def show_selection(event):
        selected_indices = listbox.curselection()  
        if selected_indices:
            selected_text = listbox.get(selected_indices[0])
            createClientSaler(selected_text)

    listbox = tk.Listbox(root, height=len(magaz.salers),font=FONT_2)
    listbox.pack(padx=PADX, pady=PADY, fill="both",anchor="center")
    for saler in magaz.salers:
        listbox.insert(tk.END, saler)  
    label = tk.Label(root, text="Выберите элемент",font=FONT_2)
    label.pack(expand=True,pady=5)
    listbox.bind("<<ListboxSelect>>", show_selection)
    btnBack = tk.Button(root,text="Go Back",font=FONT_3,command=lambda:createLogin())
    btnBack.pack(expand=True, fill="both", padx=PADX, pady=PADY)

def createLoginLogout():
    clearWindow()
    root.title("Login / Logout")
    btnLogin = tk.Button(root,text="login",font=FONT_2,command=lambda:createLogin())
    btnLogout = tk.Button(root,text="logout",font=FONT_2,command=lambda:createLogout())
    btnLogin.pack(expand=True, fill="both", padx=PADX, pady=PADY)
    btnLogout.pack(expand=True, fill="both", padx=PADX, pady=PADY)
    root.mainloop()

def createRoot():
    global root 
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    icon = tk.PhotoImage(file=ICON_4)
    root.iconphoto(True,icon)

def main():
    createStore()
    createRoot()
    createLoginLogout()

def registrate(var,entName,entAdress=None):
    typeUser = var.get()
    name = entName.get()
    adress = entAdress if entAdress == None else entAdress.get()
    if "Buyer" == typeUser:
        if not name or not adress:
            ms.showerror("Error","Enter name and adress!")
            return None
        try:
            magaz.add_user(Buyer(name,adress))
            createClientBuyer(name)
        except ValueError:
            ms.showerror("Error","User with this name was create!")
    elif "Saler" == typeUser:
        if not name:
            ms.showerror("Error","Enter name!")
            return None
        try:
            magaz.add_user(Saler(name))
            createClientSaler(name)
        except ValueError:
            ms.showerror("Error","User with this name was create!")

if __name__ == "__main__":
    main() 


