import unittest
from magazin import Magazin
from buyer import Buyer
from saler import Saler
from product import Product
from order import Order

class TestMagazin(unittest.TestCase):
    def setUp(self):
        Saler.names.clear()
        self.buyer1 = Buyer("Alice", "123 Main St", 5000.0)
        self.buyer2 = Buyer("Bob", "456 Elm St", 3000.0)
        
        self.product1 = Product("Laptop", 1000.0, 10)
        self.product2 = Product("Phone", 500.0, 20)
        
        self.saler1 = Saler("TechStore" ,1000,self.product1, self.product2)
        self.saler2 = Saler("GadgetShop" ,1000, self.product2)
        
        self.magazin = Magazin("SuperStore", [self.buyer1, self.buyer2], [self.saler1, self.saler2])
    
    def test_singleton(self):
        magazin2 = Magazin("AnotherStore", [], [])
        self.assertIs(self.magazin, magazin2)
    
    def test_search_salers(self):
        salers = list(self.magazin.search_salers("Phone"))
        self.assertIn(self.saler1, salers)
        self.assertIn(self.saler2, salers)
    
    def test_transaction_successful(self):
        self.magazin.transaction("TechStore", "Phone", "Alice", 2)
        self.assertEqual(self.buyer1.money, 4000)
        self.assertEqual(self.saler1.money, 2000)
        self.assertEqual(self.product2.count, 18)
        self.assertEqual(len(self.magazin.orders), 1)
    
    def test_transaction_invalid_saler(self):
        with self.assertRaises(ValueError):
            self.magazin.transaction("NonExistentSaler", "Phone", "Alice", 2)
    
    def test_transaction_invalid_product(self):
        with self.assertRaises(ValueError):
            self.magazin.transaction("TechStore", "Tablet", "Alice", 2)
    
    def test_transaction_invalid_buyer(self):
        with self.assertRaises(ValueError):
            self.magazin.transaction("TechStore", "Phone", "NonExistentBuyer", 2)
    
    def test_transaction_not_enough_money(self):
        with self.assertRaises(ValueError):
            self.magazin.transaction("TechStore", "Laptop", "Bob", 20)
    
    def test_transaction_not_enough_stock(self):
        with self.assertRaises(ValueError):
            self.magazin.transaction("TechStore", "Phone", "Alice", 50)
    
    def test_repr(self):
        repr_str = repr(self.magazin)
        result = f"{self.magazin._Magazin__name}/{self.magazin._Magazin__buyers}/{self.magazin._Magazin__salers}"
        self.assertEqual(repr_str,result)
if __name__ == "__main__":
    unittest.main()